import { useDispatch, useSelector } from "react-redux";
import { useEffect } from "react";
import { thunkUserReviews } from "../../store/review";
import OpenModalButton from "../OpenModalButton";
import DeleteReview from "./DeleteReview";
import EditReview from "./EditReview";


const UserReviews = () => {
    const dispatch = useDispatch()
    const reviewsObj = useSelector(state => state.review.currentUserReviews)
    const reviews = Object.values(reviewsObj)


    useEffect(() => {
        dispatch(thunkUserReviews())
    }, [dispatch])

    if (!reviews) return "loading.."
    return (
        <div>
            <h1>HELLO FROM USER REVIEWS</h1>
            {reviews.map(review => (
                <div>
                    <div>
                        review id: {review.id}
                        <div>
                            Restaurant id: {review.restaurant_id}
                        </div>
                        <div>
                            review rating: {review.rating}
                        </div>
                        <div>
                            review review_text: {review.review_text}
                        </div>
                    </div>
                    <div>
                        <OpenModalButton
                            buttonText="Edit"
                            modalComponent={<EditReview review={review} />}
                        />
                    </div>
                    <div>
                        <OpenModalButton
                            buttonText="Delete"
                            modalComponent={<DeleteReview review={review} />}
                        />
                    </div>

                    <br />
                </div>
            ))}
        </div>

    )
}



export default UserReviews;
