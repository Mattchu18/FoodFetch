// const GET_ONE_DISH = "dish/oneDish"
const GET_ALL_DISHES = "dish/allDishes"
const GET_ALL_RESTAURANT_DISHES = "dish/allRestaurantDishes"
const CREATE_DISH = "dish/createDish"
const DELETE_DISH = "dish/deleteDish"
const EDIT_DISH = "dish/editDish"


// const getOneDish = (dish) => ({
//     type: GET_ONE_DISH,
//     dish
// })

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


export const thunkAllRestaurantDishes = (restaurantId) => async (dispatch) => {
    const response = await fetch(`/api/restaurants/${restaurantId}/dishes`)
    if (response.ok) {
        const data = await response.json()
        dispatch(getAllRestaurantDishes(data))
    }
}


const initialState = { allRestaurantDishes: {} }
const dishReducer = (state = initialState, action) => {
    switch (action.type) {
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
        default: return state
    }
}

export default dishReducer