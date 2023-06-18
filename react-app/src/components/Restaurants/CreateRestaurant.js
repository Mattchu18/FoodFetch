import { useEffect } from "react";
import RestaurantForm from "./RestaurantForm";
import { useDispatch, useSelector } from "react-redux";

const CreateRestaurant = () => {
    // const user = useSelector(state => state.session.user)

    // console.log(typeof user.id)

    // useEffect(() => {

    // }, [dispatch])
    // console.log(user)

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

    return (
        <RestaurantForm
            restaurant={restaurant}
            formType="Create Restaurant"
        />
    )
}

export default CreateRestaurant
