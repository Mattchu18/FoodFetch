import RestaurantForm from "./RestaurantForm";


const EditRestaurant = ({ restaurant }) => {

    return (
        <RestaurantForm
        restaurant={restaurant}
        formType="Edit Restaurant"
        />
    )
}


export default EditRestaurant
