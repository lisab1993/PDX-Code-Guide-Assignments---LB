// when the page opens, there will be no cats. 
// the user selects something from the drop down
// the user presses the go button
// a wild cat picture appears





let app = new Vue({
    el: "#app",
    data: {
        output: "",//this will be the picture the user sees at the end
        selected_category: "5",//this is the category selected from the dropdown
        selected_breed: "abys",
        categories: [],//this is to populate the drop down.
        breeds: [],
    },
    methods: {
        get_kitty: function () {
            axios({
                method: 'get',
                url: "https://api.thecatapi.com/v1/images/search",
                params: {
                    category_ids: this.selected_category,
                    breed_ids: this.selected_breed,
                }//closes params
            }).then((response) => {
                console.log(response.data)
                if (response.data.length === 0) {
                    this.output = "https://http.cat/404"
                } else {
                    this.output = response.data[0].url
                }
            })//closes .then
        }//closes the get_kitty function,//closes axios for get_kitty
    },//closes methods

    created: function () {
        axios({
            method: "get",
            url: "https://api.thecatapi.com/v1/categories",
        }).then((response) => {
            console.log(response.data)// code was ran successfully
            this.categories = response.data

        }),//closes response
        axios({
            method: "get",
            url: "https://api.thecatapi.com/v1/breeds",

        }).then((response) => {
            console.log(response.data)
            this.breeds = response.data
        })

    }//closes created
})//closes app


 //within the created lifecycle hook, add another axios to send the request for the categories, and then link it to the drop downs.
 //assign the data in the response to the app's categories.

 //remember to to get the data first and check everything.

