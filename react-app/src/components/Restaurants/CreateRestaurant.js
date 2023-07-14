import { useEffect } from "react";
import RestaurantForm from "./RestaurantForm";
import { useDispatch, useSelector } from "react-redux";

const CreateRestaurant = () => {
    const user = useSelector(state => state.session.user)



    // useEffect(() => {

    // }, [dispatch])
    //

    const restaurant = {
        "name": "",
        "address": "",
        "phone_number": "",
        "cuisine_type": "",
        "opening_time": "",
        "closing_time": "",
        "image": "",
        "header_image": ""
        // "user_id": user.id
    }

    if (!user) return "Please log in as a Restaurant Owner to view this feature"
    return (
        <RestaurantForm
            restaurant={restaurant}
            formType="Create Restaurant"
        />
    )
}

export default CreateRestaurant
