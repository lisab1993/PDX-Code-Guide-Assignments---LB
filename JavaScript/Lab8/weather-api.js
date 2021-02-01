

let app = new Vue({
  el: "#app",
  data: {
    today_date: "",
    today_time: "",

    today_celsius: "",
    today_farenheit: "",

    current_weather: "",
    today_icon: "",

    today_feels_like_farenheit: "",
    today_feels_like_celsius: "",

    today_humidity: "",
    today_pressure: "",

    today_metric_wind_speed: "",
    today_us_wind_speed: "",

    forecast: [],
  },
  methods: {
    //this method should have been hoisted, but wasn't.
    //Uncaught (in promise) ReferenceError: get_date is not defined
    // at weather-api.js:114

    // get_date: function(date){
    //   let converted_date = new Date(date * 1000)
    //   return converted_date
    // }
    // let unix_dates = response.data.daily[i].dt
    // let dates = get_date(unix_dates)
  },
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

        // today's datetime
        let unix_timestamp = response.data.current.dt
        //current date 
        let datetime = new Date(unix_timestamp * 1000)
        let months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        let today_month = datetime.getMonth() + 1
        today_month = months[today_month]
        this.today_date = `${today_month}-${datetime.getDate()}-${datetime.getFullYear()}`
        //current time 
        let hours = datetime.getHours()
        let real_hours = datetime.getHours()
        let minutes = datetime.getMinutes()
        if(hours === 0){
          real_hours = 12
        } else if (hours > 13) {
          real_hours = hours - 12
        } 

        let time_of_day = "AM"
        if(hours >= 12){
          time_of_day = "PM"
        } 
        this.today_time = `${real_hours}:${minutes}${time_of_day}`
        
        // current temperature - celsius (converted from Kelvin)
        let c_Temp = parseInt(response.data.current.temp) - 273.15
        c_Temp = Math.round(c_Temp)
        this.today_celsius = `${c_Temp}°C`

        // current temperature - farenheit
        let f_Temp = ((parseInt(response.data.current.temp) - 273.15) * 1.8) + 32
        f_Temp = Math.round(f_Temp)
        this.today_farenheit = `${f_Temp}°F`

        // current weather
        this.current_weather = response.data.current.weather[0].description

        // icon for current weather
        let icon_data = response.data.current.weather[0].icon// 50n
        this.today_icon = `http://openweathermap.org/img/wn/${icon_data}.png`

        // currently feels_like in farenheit and celsius
        let feels_like = response.data.current.feels_like
        let feels_like_farenheit = Math.round(((parseInt(feels_like) - 273.15) * 1.8) + 32)
        this.today_feels_like_farenheit = `${feels_like_farenheit}°F`

        feels_like_celsius = Math.round(parseInt(feels_like) - 273.15)
        this.today_feels_like_celsius = `${feels_like_celsius}°C`

        // current humidity
        let today_humidity = response.data.current.humidity
        this.today_humidity = `${today_humidity}%`

        // current pressure
        let today_pressure = response.data.current.pressure
        this.today_pressure= `${today_pressure} hPa`

        // current wind_speed in metric and us 
        let wind_speed = response.data.current.wind_speed
        this.today_metric_wind_speed = wind_speed
        this.today_us_wind_speed = parseInt(wind_speed) * 2.237

        // forecast information
        // forecast dates
        let weekdays = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        for (let i = 1; i < response.data.daily.length; i++) {
          let unix_dates = response.data.daily[i].dt
          let dates_full = new Date(unix_dates * 1000)
          let forecast_weekday = dates_full.getDay()
          forecast_weekday = weekdays[forecast_weekday]
          let forecast_date = dates_full.getDate()
          if (forecast_date < 10) {
            forecast_date = "0" + forecast_date
          }
          let dates = `${forecast_weekday}/${forecast_date}`

          // forecast temperature (hi and low in farenheit and celsius)
          let unix_max_temp = response.data.daily[i].temp.max
          let forecast_max_temp_faren = Math.round(((parseInt(unix_max_temp) - 273.15) * 1.8) + 32)
          forecast_max_temp_faren = `${forecast_max_temp_faren}°F`
          let forecast_max_temp_cels = Math.round(parseInt(unix_max_temp) - 273.15)
          forecast_max_temp_cels = `${forecast_max_temp_cels}°C`

          let unix_min_temp = response.data.daily[i].temp.min
          let forecast_min_temp_faren = Math.round(((parseInt(unix_min_temp) - 273.15) * 1.8) + 32)
          forecast_min_temp_faren = `${forecast_min_temp_faren}°F`
          let forecast_min_temp_cels = Math.round(parseInt(unix_min_temp) - 273.15)
          forecast_min_temp_cels = `${forecast_min_temp_cels}°C`

          // forecast weather condition and icon
          let forecast_weather_condition = response.data.daily[i].weather[0].description
          let forecast_icon_data = response.data.daily[i].weather[0].icon
          let forecast_icon = `http://openweathermap.org/img/wn/${forecast_icon_data}.png`

          //rain chance and humidity
          let forecast_humidity = response.data.daily[i].humidity
          forecast_humidity = `${forecast_humidity}%`
          let forecast_rain_chance = response.data.daily[i].pop
          forecast_rain_chance = `${forecast_rain_chance}%`

          //these variables hold various portions of the data; they are pushed into the forecast array to be called in html
          this.forecast.push({
            forecast_dates: dates,

            forecast_max_temp_faren: forecast_max_temp_faren,
            forecast_max_temp_cels: forecast_max_temp_cels,

            forecast_min_temp_faren: forecast_min_temp_faren,
            forecast_min_temp_cels: forecast_min_temp_cels,

            forecast_weather_condition: forecast_weather_condition,
            forecast_icon: forecast_icon,

            forecast_humidity: forecast_humidity,
            forecast_rain_chance: forecast_rain_chance,
          })
        }
      })
    })
  }//closes created
})//closes app


