import { useDispatch } from "react-redux";
import { useEffect, useState } from "react";
import { useHistory } from "react-router-dom";
import { thunkCreateReview } from "../../store/review";
import { useModal } from "../../context/Modal";

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

        if (review_text.length < 5) errors.review_text = "Review text needs to be at least 5 characters"
        if (!rating) errors.rating = "Rating must be from 1-5 stars"
        setValidationErrors(errors)

        if (formType === "Create Review" && !Object.keys(errors).length) {
            await dispatch(thunkCreateReview(review))
                .then(closeModal)

            history.push(`/`)
        }

        if (!!Object.keys(errors).length) return
    }

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <h1>Add a Public Review</h1>
            </div>
            {validationErrors.rating ? (<p className="errors" >{validationErrors.rating}</p>) : null}
            <div>
                {arr} Stars
            </div>
            <div>
                <textarea
                    className="textInfo"
                    type="text"
                    value={review_text}
                    placeholder="Helpful reviews mention specific items and describe their quality and taste."
                    onChange={e => setReview_text(e.target.value)}
                />
            </div>
            <div>
                <button type="submit" disabled={!review_text || !rating} >Submit your Review</button>
            </div>

        </form>

    )

}

export default ReviewForm
