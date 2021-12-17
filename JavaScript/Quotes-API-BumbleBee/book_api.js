let app = new Vue({
    el: '#app',
    data: {
        results: []
    },
    methods: {
        loadQuotes: function () {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotd',
                headers: {
                    'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'
                }
            }).then(response => console.log(response))
        }
    }
})