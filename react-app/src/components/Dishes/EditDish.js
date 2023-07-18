import DishForm from "./DishForm";

const EditDish = ({ dish, restaurantId }) => {

    return (
        <DishForm
        dish={dish}
        restaurantId={restaurantId}
        formType="Edit Dish"
        />
    )
}

export default EditDish
