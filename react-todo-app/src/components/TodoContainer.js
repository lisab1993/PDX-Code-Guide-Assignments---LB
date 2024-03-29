import React from "react"
import { render } from "react-dom"
import TodosList from "./TodosList"
import Header from "./Header"

class TodoContainer extends React.Component {
    state = {
        todos: [
            {
                id: 1,
                title: "Setup development environment",
                completed: true
            },
            {
                id: 2,
                title: "Develop website and add content",
                completed: false
            },
            {
                id: 3,
                title: "Deploy to live server",
                completed: false
              }
        ],
    }
    handleChange = (id) => {
        this.setState( prevState => ({
            todos: this.state.todos.map(todo => {
                if (todo.id === id) {
                    todo.completed = !todo.completed
                }
                return todo
            })
        }))
    }
    render() {
        return (
            //React.Fragment allows you to return JSX formatting without it being overwritten by a div (or something else)
            <React.Fragment>
                <Header />
                <TodosList todos={this.state.todos} handleChangeProps={this.handleChange} />
            </React.Fragment>
        )
    }
}
export default TodoContainer
