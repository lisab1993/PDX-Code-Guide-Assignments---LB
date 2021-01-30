

let app = new Vue({
  el: "#app",
  data: {
    celsius: "",
    farenheit: "",
    current_weather: "",
    forecast: [],

    date: "",
    time: "",
    feels_like_farenheit: "",
    feels_like_celsius: "",
    icon: "",

    humidity: "",
    metric_wind_speed: "",
    us_wind_speed: "",

  },//closes data
  created: function () {//this function runs when the page is created
    navigator.geolocation.getCurrentPosition(position => {//we the geolocation API
      // console.log(position)// position holds all parts of the coordinates, including latitude, longitude, and altitude
      // console.log(position.coords.latitude)
      // console.log(position.coords.longitude)
      axios({
        method: 'get',
        url: 'https://api.openweathermap.org/data/2.5/onecall',
        params: {
          lat: position.coords.latitude,
          lon: position.coords.longitude,
          exclude: 'minutely,hourly,alerts',
          appid: openweathermap_api_key,
          lang: 'English',
          //there's one for units, but it's going unused because I want to use Farenheit and
        }

      }).then(response => {
        console.log(response.data)

        //current temperature - celsius (converted from Kelvin)
        let c_Temp = parseInt(response.data.current.temp) - 273.15
        let c_Temp_Rounded = Math.round(c_Temp)
        this.celsius = `${c_Temp_Rounded}℃`

        //current temperature - farenheit
        let f_Temp = ((parseInt(response.data.current.temp) - 273.15) * 1.8) + 32
        let f_Temp_Rounded = Math.round(f_Temp)
        this.farenheit = `${f_Temp_Rounded}℉`

        //datetime
        let unix_timestamp = response.data.current.dt
        // date 
        this.datetime = new Date(unix_timestamp * 1000)
        this.date = `${this.datetime.getMonth() + 1}-${this.datetime.getDate()}-${this.datetime.getFullYear()}`
        // time 
        let hours = this.datetime.getHours()
        let minutes = this.datetime.getMinutes()
        if (hours > 12) {
          hours = hours - 12
        } else {
          hours = hours
        }
        this.time = `${hours}:${minutes}`


        //current weather
        this.current_weather = response.data.current.weather[0].main

        //icon for current weather
        let icon_data = response.data.current.weather[0].icon// 50n
        this.icon = `http://openweathermap.org/img/wn/${icon_data}.png`

        // feels_like in celsius and farenheit
        let feels_like = response.data.current.feels_like
        let pre_feels_like_celsius = Math.round(parseInt(feels_like) - 273.15)
        this.feels_like_celsius = `${pre_feels_like_celsius}℃`

        let pre_feels_like_farenheit = Math.round(((parseInt(feels_like) - 273.15) * 1.8) + 32)
        this.feels_like_farenheit = `${pre_feels_like_farenheit}℉`


        // humidity
        this.humidity = response.data.current.humidity

        // wind_speed in metric and us 
        let wind_speed = response.data.current.wind_speed
        this.metric_wind_speed = wind_speed
        this.us_wind_speed = parseInt(wind_speed) * 2.237

        //forecast information
        for (let i=1; i<response.data.daily.length; i++) {
          this.forecast.push({
            dates: response.data.daily[i].dt,
            max_temp: response.data.daily[i].temp.max,
            min_temp: response.data.daily[i].temp.min,
            weather_condition: response.data.daily[i].weather[0].main, 
          })
        }
      })
    })
  }//closes created
})//closes app
