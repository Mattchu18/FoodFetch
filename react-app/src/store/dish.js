const GET_ONE_DISH = "dish/oneDish"
const GET_ALL_DISHES = "dish/allDishes"
const GET_ALL_RESTAURANT_DISHES = "dish/allRestaurantDishes"
const CREATE_DISH = "dish/createDish"
const DELETE_DISH = "dish/deleteDish"
const EDIT_DISH = "dish/editDish"


const getOneDish = (dish) => ({
    type: GET_ONE_DISH,
    dish
})

const getAllDishes = (dishes) => ({
    type: GET_ALL_DISHES,
    dishes
})

const getAllRestaurantDishes = (dishes) => ({
    type: GET_ALL_RESTAURANT_DISHES,
    dishes
})

const createDish = (dish) => ({
    type: CREATE_DISH,
    dish
})

const deleteDish = (dish) => ({
    type: DELETE_DISH,
    dish
})

const editDish = (dish) => ({
    type: EDIT_DISH,
    dish
})


// export const thunkOneDish = (dishId) => {

// }
export const thunkAllDishes = () => async (dispatch) => {
    const response = await fetch('/api/dishes/all')
    if (response.ok) {
        const data = await response.json()
        dispatch(getAllDishes(data))
    }

}

export const thunkAllRestaurantDishes = (restaurantId) => async (dispatch) => {
    const response = await fetch(`/api/restaurants/${restaurantId}/dishes`)
    if (response.ok) {
        const data = await response.json()
        dispatch(getAllRestaurantDishes(data))
    }
}

// create a dish
export const thunkCreateDish = (formData, restaurantId) => async (dispatch) => {
    const response = await fetch(`/api/restaurants/${restaurantId}/dishes`, {
        method: "POST",
        body: formData
    })
    if (response.ok) {
        const {resPost} = await response.json()
        dispatch(createDish(resPost))
    }
}

// delete a dish
export const thunkDeleteDish = ( dish ) => async (dispatch) => {
    const response = await fetch(`/api/restaurants/${restaurantId}/dishes/${dish.id}/`, {
        method: "DELETE"
    })
    if (response.ok) {
        const data = await response.json()
        dispatch(deleteDish(data))
    }
}

// update a dish
export const thunkEditDish = ( dish, restaurantId, formData ) => async (dispatch) => {
    // console.log("this is dish========>",dish)
    const response = await fetch(`/api/restaurants/${restaurantId}/dishes/${dish.id}`, {
        method: "PUT",
        body: formData
    })
    if (response.ok) {
        const {resPost} = await response.json()
        dispatch(editDish(resPost))
    }
}


const initialState = { allDishes: {}, allRestaurantDishes: {} }
const dishReducer = (state = initialState, action) => {
    switch (action.type) {
        case GET_ALL_DISHES: {
            const newState = {}
            const allDishes = action.dishes
            allDishes.forEach(dish => {
                newState[dish.id] = dish
            })
            return {
                ...state,
                allDishes: newState
            }
        }
        case GET_ALL_RESTAURANT_DISHES: {
            const newState = {}
            const allRestaurantDishes = action.dishes
            allRestaurantDishes.forEach(dish => {
                newState[dish.id] = dish
            })
            return {
                ...state,
                allRestaurantDishes: newState
            }
        }
        case CREATE_DISH: {
            const newState = {}
            const newDish = action.dish
            newState[newDish.id] = newDish
            return {
                ...state,
                allDishes: { ...state.allDishes, ...newState}
            }
        }
        case EDIT_DISH: {
            const newState = {}
            const newDish = action.dish
            newState[newDish.id] = newDish
            return {
                allRestaurantDishes: { ...state.allRestaurantDishes, ...newState},
                allDishes: { ...state.allDishes }
            }
        }
        case DELETE_DISH: {
            const newState = { ...state.allRestaurantDishes }
            const newAllDishesState = { ...state.allDishes }
            const dishId = action.dish.dishId
            delete newState[dishId]
            delete newAllDishesState[dishId]
            return {
                allRestaurantDishes: newState,
                allDishes: newAllDishesState
            }
        }
        default: return state
    }
}

export default dishReducer
