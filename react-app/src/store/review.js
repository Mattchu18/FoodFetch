const GET_USER_REVIEWS = "review/userReviews"
const GET_ALL_REVIEWS = "review/allReviews"
const CREATE_REVIEW = "review/createReview"
const DELETE_REVIEW = "review/deleteReview"


const getAllReviews = (reviews) => ({
    type: GET_ALL_REVIEWS,
    reviews
})

const getUserReviews = (reviews) => ({
    type: GET_USER_REVIEWS,
    reviews
})

const createReview = (review) => ({
    type: CREATE_REVIEW,
    review
})

const deleteReview = (review) => ({
    type: DELETE_REVIEW,
    review
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


export const thunkCreateReview = (review) => async (dispatch) => {
    const response = await fetch(`/api/restaurants/${review.restaurant_id}/reviews`, {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(review)
    })
    if (response.ok) {
        const data = await response.json()
        dispatch(createReview(data))
    }
}


export const thunkDeleteReview = (review) => async (dispatch) => {
    const response = await fetch(`/api/reviews/${review.id}/delete`, {
        method: "DELETE"
    })
    if (response.ok) {
        const data = await response.json()
        dispatch(deleteReview(data))
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
        case CREATE_REVIEW: {
            const newState = {}
            const newReview = action.review
            newState[newReview.id] = newReview
            return {
                ...state,
                singleReview: newState,
                allReviews: { ...state.allReviews, ...newState}
            }
        }
        case DELETE_REVIEW: {
            const newState = { ...state.currentUserReviews }
            const newSingleState = { ...state.singleReview}
            const reviewId = action.review.reviewId
            delete newState[reviewId]
            delete newSingleState[reviewId]
            return {
                currentUserReviews: newState,
                singleReview: newSingleState,
                allReviews: { ...state.allReviews }
            }
        }
        default: return state
    }

}

export default reviewsReducer;
