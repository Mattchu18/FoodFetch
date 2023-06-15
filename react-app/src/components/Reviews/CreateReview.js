import ReviewForm from "./ReviewForm";


const CreateReview = ({ restaurantId }) => {
    const review = {
        review_text: "",
        rating: "",
        restaurant_id: restaurantId
    }

    return (
        <>
            <ReviewForm
                review={review}
                formType={"Create review"}
        />
        </>

    )
}

export default CreateReview
