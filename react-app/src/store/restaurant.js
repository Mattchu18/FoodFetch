const GET_ONE_RESTAURANT = "restaurant/oneRestaurant"
const GET_ALL_RESTAURANTS = "restaurant/allRestaurants"
const GET_USER_RESTAURANTS = "restaurant/userRestaurants"
const CREATE_RESTAURANT = "restaurant/createRestaurant"
const DELETE_RESTAURANT = "restaurant/deleteRestaurant"
const EDIT_RESTAURANT = "restaurant/editRestaurant"


const getOneRestaurant = (restaurant) => ({
    type: GET_ONE_RESTAURANT,
    restaurant
})

const getAllRestaurants = (restaurants) => ({
    type: GET_ALL_RESTAURANTS,
    restaurants
})

const getUserRestaurants = (restaurants) => ({
    type: GET_USER_RESTAURANTS,
    restaurants
})

const createRestaurant = (restaurant) => ({
    type: CREATE_RESTAURANT,
    restaurant
})

const deleteRestaurant = (restaurant) => ({
    type: DELETE_RESTAURANT,
    restaurant
})

const editRestaurant = (restaurant) => ({
    type: EDIT_RESTAURANT,
    restaurant
})


export const thunkOneRestaurant = (restaurantId) => async (dispatch) => {
    const response = await fetch(`/api/restaurants/${restaurantId}`)
    if (response.ok) {
        const data = await response.json()
        dispatch(getOneRestaurant(data))
    }
}

export const thunkAllRestaurants = () => async (dispatch) => {
    const response = await fetch('/api/restaurants')
    if (response.ok) {
        const data = await response.json()
        dispatch(getAllRestaurants(data))
    }
}


export const thunkUserRestaurants = () => async (dispatch) => {
    const response = await fetch('/api/restaurants/user')
    if (response.ok) {
        const data = await response.json()
        dispatch(getUserRestaurants(data))

    }

}


const initialState = { currentUserRestaurants: {}, singleRestaurant: {}, allRestaurants:{} }
const restaurantReducer = ( state = initialState, action ) => {
    switch (action.type) {
        case GET_ONE_RESTAURANT: {
            const newState = {}
            const newRestaurant = action.restaurant
            newState[newRestaurant.id] = newRestaurant
            return {
                ...state, singleRestaurant: newState
            }
        }
        case GET_ALL_RESTAURANTS: {
            const newState = {}
            const allRestaurants = action.restaurants
            allRestaurants.forEach(restaurant => {
                newState[restaurant.id] = restaurant
            })
            return {
                ...state,
                allRestaurants: newState
            }
        }
        case GET_USER_RESTAURANTS: {
            const newState = {}
            const userRestaurants = action.restaurants
            userRestaurants.forEach(restaurant => {
                newState[restaurant.id] = restaurant
            })
            return {
                ...state, currentUserRestaurants: newState
            }
        }
        default: return state
    }

}

export default restaurantReducer
