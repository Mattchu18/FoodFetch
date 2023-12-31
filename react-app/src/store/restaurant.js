const GET_ONE_RESTAURANT = "restaurant/oneRestaurant"
const GET_ALL_RESTAURANTS = "restaurant/allRestaurants"
const GET_USER_RESTAURANTS = "restaurant/userRestaurants"
const CREATE_RESTAURANT = "restaurant/createRestaurant"
const DELETE_RESTAURANT = "restaurant/deleteRestaurant"
const EDIT_RESTAURANT = "restaurant/editRestaurant"
const SEARCH_RESTAURANT = "restaurant/searchRestaurant"

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

const editRestaurant = (restaurant) => ({
    type: EDIT_RESTAURANT,
    restaurant
})

const deleteRestaurant = (restaurant) => ({
    type: DELETE_RESTAURANT,
    restaurant
})

const searchRestaurant = (restaurants) => ({
    type: SEARCH_RESTAURANT,
    restaurants
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

export const thunkCreateRestaurant = (restaurant) => async (dispatch) => {

    const response = await fetch('/api/restaurants/new', {
        method: "POST",
        // headers: { 'Content-Type': 'application/json' },
        // We do not JSON.stringify restaurant since the backend will not accept
        body: restaurant
    })
    if (response.ok) {
        // we picked up resPost from our Post Restaurant route
        const {resPost} = await response.json()
        dispatch(createRestaurant(resPost))
    }
}


export const thunkEditRestaurant = (formData, restaurant) => async (dispatch) => {
    const response = await fetch(`/api/restaurants/${restaurant.id}/edit`, {
        method: "PUT",
        // headers: { 'Content-Type': 'application/json' },
        body: formData
    })
    if (response.ok) {
        const {resPost} = await response.json()
        dispatch(editRestaurant(resPost))
    }
}


export const thunkDeleteRestaurant = (restaurant) => async (dispatch) => {
    const response = await fetch(`/api/restaurants/${restaurant.id}/delete`, {
        method: "DELETE"
    })
    if (response.ok) {
        const data = await response.json()
        dispatch(deleteRestaurant(data))
    }
}

export const thunkSearchRestaurant = (keyword) => async (dispatch) => {
    const response = await fetch(`/api/restaurants/search?keyword=${keyword}`)
    if (response.ok) {
        const data = await response.json()
        dispatch(searchRestaurant(data))
    }
}

const initialState = { currentUserRestaurants: {}, singleRestaurant: {}, allRestaurants: {}, searchRestaurants: {} }
const restaurantReducer = (state = initialState, action) => {
    switch (action.type) {
        case GET_ONE_RESTAURANT: {
            const newState = {}
            const newRestaurant = action.restaurant
            newState[newRestaurant.id] = newRestaurant
            return {
                ...state,
                singleRestaurant: newState
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
                ...state,
                currentUserRestaurants: newState
            }
        }
        case CREATE_RESTAURANT: {
            const newState = {}
            const newRestaurant = action.restaurant
            newState[newRestaurant.id] = newRestaurant
            return {
                ...state,
                singleRestaurant: newState,
                allRestaurants: { ...state.allRestaurants, ...newState }
            }
        }
        case EDIT_RESTAURANT: {
            const newState = {}
            const newRestaurant = action.restaurant
            newState[newRestaurant.id] = newRestaurant
            return {
                currentUserRestaurants: { ...state.currentUserRestaurants, ...newState },
                singleRestaurant: newState,
                allRestaurants: { ...state.allRestaurants }
            }
        }
        case DELETE_RESTAURANT: {
            const newState = { ...state.currentUserRestaurants }
            const newSingleState = { ...state.singleRestaurant }
            const restaurantId = action.restaurant.restaurantId
            delete newState[restaurantId]
            delete newSingleState[restaurantId]
            return {
                currentUserRestaurants: newState,
                singleRestaurant: newSingleState,
                allRestaurants: { ...state.allRestaurants }
            }
        }
        case SEARCH_RESTAURANT: {
            const newState = {}
            const searchRestaurants = action.restaurants
            searchRestaurants.forEach(restaurant => {
                newState[restaurant.id] = restaurant
            })
            return {
                ...state,
                searchRestaurants: newState
            }
        }

        default: return state
    }

}

export default restaurantReducer
