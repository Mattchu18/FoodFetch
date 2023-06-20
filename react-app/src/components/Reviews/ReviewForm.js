import { useDispatch } from "react-redux";
import { useEffect, useState } from "react";
import { useHistory } from "react-router-dom";
import { thunkCreateReview, thunkEditReview,thunkUserReviews, thunkAllReviews } from "../../store/review";
import { useModal } from "../../context/Modal";
import "./ReviewForm.css"

const ReviewForm = ({ review, formType, disabled }) => {
    const dispatch = useDispatch()
    const history = useHistory()

    const [review_text, setReview_text] = useState(review?.review_text)
    const [rating, setRating] = useState(review?.rating)
    const [activeRating, setActiveRating] = useState(rating)
    const [validationErrors, setValidationErrors] = useState('')
    const { closeModal } = useModal()

    useEffect(() => {
        setActiveRating(rating)
    }, [rating])

    const onChange = (num) => {
        setRating(parseInt(num))
    }

    const handleMouseEnter = (index) => {
        if (!disabled) {
            setActiveRating(index + 1)
        }
    }

    const handleMouseLeave = () => {
        if (!disabled) {
            setActiveRating(rating)
        }
    }

    const handleClick = (index) => {
        if (!disabled) {
            onChange(index + 1)
        }
    }

    let arr = []
    for (let index = 0; index < 5; index++) {
        const className = index < activeRating ? 'fas fa-star' : 'far fa-star'
        arr.push(
            <div
                className={className}
                onMouseEnter={() => handleMouseEnter(index)}
                onMouseLeave={handleMouseLeave}
                onClick={() => handleClick(index)}>
                {/* <i className={className}></i> */}
            </div>
        )
    }

    const handleSubmit = async (e) => {
        e.preventDefault()
        let errors = {}
        review = {
            ...review,
            review_text,
            rating
        }
        // console.log("this is review text length====>", review_text.length)
        if (review_text.length < 5) errors.review_text = "Review text needs to be at least 5 characters"
        if (review_text.length > 1000) errors.review_text = "Review text needs to be under 1000 characters"
        if (!rating) errors.rating = "Rating must be from 1-5 stars"
        setValidationErrors(errors)

        if (formType === "Create Review" && !Object.keys(errors).length) {
            await dispatch(thunkCreateReview(review))
            dispatch(thunkUserReviews())
            dispatch(thunkAllReviews())
                .then(closeModal)
        }

        if (formType === "Edit Review" && !Object.keys(errors).length) {
            await dispatch(thunkEditReview(review))
            dispatch(thunkUserReviews())
            dispatch(thunkAllReviews())
            .then(closeModal)
        }

        if (!!Object.keys(errors).length) return
    }

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <h1>Add a Public Review</h1>
            </div>
            {validationErrors.rating ? (<p className="errors" >{validationErrors.rating}</p>) : null}
            <div className="review-stars">
                {arr}
            </div>
            <div className="text-area-div">

            {validationErrors.review_text ? (<p className="errors" >{validationErrors.review_text}</p>) : null}
                <textarea
                    className="textInfo"
                    type="text"
                    value={review_text}
                    max='1000'
                    placeholder="Helpful reviews mention specific items and describe their quality and taste. (max: 1000 characters)"
                    onChange={e => setReview_text(e.target.value)}
                />
            </div>
            <div className="submit-review-btn">
                <button type="submit" disabled={!review_text || !rating} >Submit your Review</button>
            </div>

        </form>

    )

}

export default ReviewForm
