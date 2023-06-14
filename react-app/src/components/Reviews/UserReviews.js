import { useDispatch, useSelector } from "react-redux";
import { useEffect } from "react";
import { thunkUserReviews } from "../../store/review";


const GetUserReviews = () => {
    const dispatch = useDispatch()
    const reviewsObj = useSelector(state => state.review.currentUserReviews)
    const reviews = Object.values(reviewsObj)
    console.log("this is reviews!=====>", reviews)

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
                    <br />
                </div>
            ))}
        </div>

    )
}



export default GetUserReviews;
