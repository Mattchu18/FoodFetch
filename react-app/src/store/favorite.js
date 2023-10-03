// const GET_ALL_FAVORITES = "favorite/allFavorites"
const GET_USER_FAVORITES = "favorite/userFavorites"
const GET_RESTAURANT_FAVORITES = "favorite/restaurantFavorites"
const CREATE_FAVORITE = "favorite/createFavorite"
const DELETE_FAVORITE = "favorite/deleteFavorite"

// const getAllFavorites = (favorites) => ({
//     type: GET_ALL_FAVORITES,
//     favorites
// })

const getUserFavorites = (favorites) => ({
    type: GET_USER_FAVORITES,
    favorites
})

const getRestaurantFavorites = (favorites) => ({
    type: GET_RESTAURANT_FAVORITES,
    favorites
})

const createFavorite = (favorite) => ({
    type: CREATE_FAVORITE,
    favorite
})

const deleteFavorite = (favorite) => ({
    type: DELETE_FAVORITE,
    favorite
})


export const thunkUserFavorites = (userId) => async (dispatch) => {
    const response = await fetch(`/api/favorites/users/${userId}`)
    if (response.ok) {
        const data = await response.json()
        dispatch(getUserFavorites(data))
    }
}

export const thunkRestaurantFavorites = (restaurantId) => async (dispatch) => {
    const response = await fetch(`/api/restaurant/${restaurantId}/favorites`)
    if (response.ok) {
        const data = await response.json()
        dispatch(getRestaurantFavorites(data))
    }
}

export const thunkCreateFavorite = (restaurantId) => async (dispatch) => {
    const response = await fetch(`/api/restaurant/${restaurantId}/favorites`, {
        method: "POST"
    })
    if (response.ok) {
        const data = await response.json()
        dispatch(createFavorite(data))
    }
}

export const thunkDeleteFavorite = ( favoriteId ) => async (dispatch) => {
    const response = await fetch(`/api/favorites/${favoriteId}`, {
        method: "DELETE"
    })
    if (response.ok) {
        const data = await response.json()
        dispatch(deleteFavorite(data))
    }
}

const initialState = { userFavorites: {}, restaurantFavorites: {} }
const favoriteReducer = (state = initialState, action) => {
    switch (action.type) {
        case GET_USER_FAVORITES: {
            const newState = {}
            const userFavorites = action.favorites
            userFavorites.forEach(favorite => {
                newState[favorite.id] = favorite
            })
            return {
                ...state,
                userFavorites: userFavorites
            }
        }
        case GET_RESTAURANT_FAVORITES: {
            const newState = {}
            const restaurantFavorites = action.favorites
            restaurantFavorites.forEach(favorite => {
                newState[favorite.id] = favorite
            })
            return {
                ...state,
                restaurantFavorites: restaurantFavorites
            }
        }
        case CREATE_FAVORITE: {
            const newState= {}
            const newFavorite = action.favorite
            newState[newFavorite.id] = newFavorite
            return {
                ...state,
                userFavorites: { ...state.userFavorites, ...newState},
                restaurantFavorites: { ...state.restaurantFavorites, ...newState}

            }
        }
        case DELETE_FAVORITE: {
            const newUserFavoritesState = { ...state.userFavorites }
            const newRestaurantFavoriteState = { ...state.restaurantFavorites }
            const favoriteId = action.favorite.favoriteId
            delete newUserFavoritesState[favoriteId]
            delete newRestaurantFavoriteState[favoriteId]
            return {
                userFavorites: newUserFavoritesState,
                restaurantFavorites: newRestaurantFavoriteState
            }
        }
        default: return state
    }
}

export default favoriteReducer
