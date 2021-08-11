
let app = new Vue({
    el: '#app',
    data: {
        sayHello: 'Hello from Vue!!',
        colors: ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet'],
        userName: '',
        chosenColorDynamic: 'Yellow',
        chosenColorStatic: '',
        chosenRadioAnimalStatic: '',
        animals: ['Quokka', 'Sugar Glider', 'Mantis Shrimp'],
        chosenRadioAnimalDynamic: 'Sugar Glider',
    }
})