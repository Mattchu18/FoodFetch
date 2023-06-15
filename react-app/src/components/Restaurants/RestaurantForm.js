import { useDispatch } from "react-redux";
import { useEffect, useState } from "react";
import { useHistory } from "react-router-dom";
import { thunkCreateRestaurant, thunkEditRestaurant } from "../../store/restaurant";
import { useModal } from "../../context/Modal";


const RestaurantForm = ({ restaurant, formType, disabled }) => {
    const dispatch = useDispatch()
    const history = useHistory()

    const [name, setName] = useState(restaurant?.name)
    const [address, setAddress] = useState(restaurant?.address)
    const [phone_number, setPhone_number] = useState(restaurant?.phone_number)
    const [cuisine_type, setCuisine_type] = useState(restaurant?.cuisine_type)
    const [opening_time, setOpening_time] = useState(restaurant?.opening_time)
    const [closing_time, setClosing_time] = useState(restaurant?.closing_time)
    const [validationErrors, setValidationErrors] = useState("")

    const handleSubmit = async (e) => {
        e.preventDefault()
        let errors = {}

        restaurant = {
            ...restaurant,
            name,
            address,
            phone_number,
            cuisine_type,
            opening_time,
            closing_time
        }

        if (!name) errors.name = "Name is required"
        if (!address) errors.address = "Address is required"
        if (!phone_number) errors.phone_number = "Phone number is required"
        if (!cuisine_type) errors.cuisine_type = "Cuisine type is required"
        if (!opening_time) errors.opening_time = "Opening time is required"
        if (!closing_time) errors.closing_time = "Closing time is required"
        setValidationErrors(errors)

        if (formType === "Create Restaurant" && !Object.keys(errors).length) {
            await dispatch(thunkCreateRestaurant(restaurant))
        }

        if (!!Object.keys(errors).length) return

    }

    return (
        <form onSubmit={handleSubmit} >
            <div>
                {formType === "Create Restaurant" ? (<h1>Create your restaurant!</h1>) : (<h1>Update your restaurant!</h1>)}
            </div>
            <div>
                <input type="text"
                    value={name}
                    placeholder="Business Name"
                    onChange={e => setName(e.target.value)}
                />
            </div>
            <div>
                <input type="text"
                    value={address}
                    placeholder="Business Address"
                    onChange={e => setAddress(e.target.value)}
                />
            </div>
            <div>
                <input type="text"
                    value={phone_number}
                    placeholder="Business Phone"
                    onChange={e => setPhone_number(e.target.value)}
                />
            </div>
            <div>
                <select onChange={e => setCuisine_type(e.target.value)}>
                    <option value="">---Cuisine Type---</option>
                    <option value="American">American</option>
                    <option value="Filipino">Filipino</option>
                    <option value="Chinese">Chinese</option>
                    <option value="Italian">Italian</option>
                    <option value="Korean">Korean</option>
                    <option value="Mediterranean">Mediterranean</option>
                    <option value="Vietnamese">Vietnamese</option>
                    <option value="Peruvian">Peruvian</option>
                    <option value="Nepalese">Nepalese</option>
                    <option value="Indian">Indian</option>
                </select>
            </div>

            <div>
                <input
                    type="time"
                    value={opening_time}
                    onChange={e => setOpening_time(e.target.value)}
                />
            </div>
            <div>
                <input
                    type="time"
                    value={closing_time}
                    onChange={e => setClosing_time(e.target.value)}
                />
            </div>
            <div>
                <button type="submit">Submit</button>
            </div>
        </form>

    )
}

export default RestaurantForm
