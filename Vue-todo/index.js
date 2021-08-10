

let app = new Vue({
    el: '#app',
    data: {
        inputText: '',
        incompleteItems: [],
        completeItems: []
    }, 
    methods: {
        addTask: function() {
            let item = {
                text: this.inputText,
            }
            console.log(item)
            this.incompleteItems.push(item)
            this.inputText = ''
        },
        completeTask: function(index) {
            let item = this.incompleteItems[index]
            this.incompleteItems.splice(index, 1)
            this.completeItems.push(item)
        },
        deleteIncomplete: function(index) {
            this.incompleteItems.splice(index, 1)
        },
        deleteComplete: function(index) {
            this.completeItems.splice(index, 1)
        },
    }
})