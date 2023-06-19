import ReviewForm from "./ReviewForm";


const CreateReview = ({ restaurantId }) => {
    const review = {
        review_text: "",
        rating: "",
        restaurant_id: restaurantId
    }

    console.log("THis is restaurant Id====", restaurantId)
    return (
        <>
            <ReviewForm
                review={review}
                formType={"Create Review"}
        />
        </>

    )
}

export default CreateReview
