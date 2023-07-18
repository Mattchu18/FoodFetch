import DishForm from "./DishForm"
import { useSelector } from "react-redux";

const CreateDish = ( {restaurantId} ) => {
    const user = useSelector(state => state.session.user)

    const dish = {
        "name": "",
        "description": "",
        "price": "",
        "dish_image": ""
    }
    if (!user) return "Please log in as a Restaurant Owner to view this feature"
    return (
        <DishForm
        dish={dish}
        restaurantId={restaurantId}
        formType="Create Dish"
        />
    )
}

export default CreateDish
