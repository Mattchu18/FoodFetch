const GET_USER_REVIEWS = "review/userReviews"
const GET_ALL_REVIEWS = "review/allReviews"


const getAllReviews = (reviews) => ({
    type: GET_ALL_REVIEWS,
    reviews
})

const getUserReviews = (reviews) => ({
    type: GET_USER_REVIEWS,
    reviews
})


export const thunkAllReviews = () => async (dispatch) => {
    const response = await fetch('/api/reviews')
    if (response.ok) {
        const data = await response.json()
        dispatch(getAllReviews(data))
    }
}


export const thunkUserReviews = () => async (dispatch) => {
    const response = await fetch('/api/reviews/user')
    if (response.ok) {
        const data = await response.json()
        dispatch(getUserReviews(data))
    }
}


const initialState = { currentUserReviews: {}, singleReview: {}, allReviews: {}}
const reviewsReducer = ( state = initialState, action ) => {
    switch (action.type) {
        case GET_ALL_REVIEWS: {
            const newState = {}
            const allReviews = action.reviews
            allReviews.forEach(review => {
                newState[review.id] = review
            })
            return {
                ...state,
                allReviews: newState
            }
        }
        case GET_USER_REVIEWS: {
            const newState = {}
            const allReviews = action.reviews
            allReviews.forEach(review => {
                newState[review.id] = review
            })
            return {
                ...state,
                currentUserReviews: newState
            }
        }
        default: return state
    }

}

export default reviewsReducer;
