import DishForm from "./DishForm"

const CreateDish = () => {
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
        formType="Create Dish"
        />
    )
}

export default CreateDish
