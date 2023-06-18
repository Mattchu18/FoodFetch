import { useDispatch } from "react-redux";
import { useEffect, useState } from "react";
import { useHistory } from "react-router-dom";
import { thunkCreateRestaurant, thunkEditRestaurant } from "../../store/restaurant";
import { useModal } from "../../context/Modal";
import './RestaurantForm.css'

const RestaurantForm = ({ restaurant, formType, disabled }) => {
    const dispatch = useDispatch()
    const history = useHistory()
    const { closeModal } = useModal()
    const [name, setName] = useState(restaurant?.name)
    const [address, setAddress] = useState(restaurant?.address)
    const [phone_number, setPhone_number] = useState(restaurant?.phone_number)
    const [cuisine_type, setCuisine_type] = useState(restaurant?.cuisine_type)
    const [opening_time, setOpening_time] = useState(restaurant?.opening_time)
    const [closing_time, setClosing_time] = useState(restaurant?.closing_time)
    const [image, setImage] = useState(restaurant?.image || "")
    const [header_image, setHeader_image] = useState(restaurant?.header_image || "")
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
            closing_time,
            image,
            header_image
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
            history.push("/restaurants/user")
        }
        if (formType === "Edit Restaurant" && !Object.keys(errors).length) {
            await dispatch(thunkEditRestaurant(restaurant))
                .then(closeModal)
        }

        if (!!Object.keys(errors).length) return

    }

    return (
        <div id="create-restaurant-form">
            <form onSubmit={handleSubmit} >
                <div>
                    {formType === "Create Restaurant" ? (<h1>Create your restaurant!</h1>) : (<h1>Update your restaurant!</h1>)}
                </div>
                <div>
                    <div>
                        {/* <div className="question-header">
                            <h2>What is your business' name? <span style={{ color: "red" }}>*</span></h2>
                        </div> */}
                        {validationErrors.name ? (<p className="errors">{validationErrors.name}</p>) : null}
                        <input type="text"
                            value={name}
                            placeholder="Business Name"
                            onChange={e => setName(e.target.value)}

                        />
                    </div>
                </div>
                <div>
                    {/* <div className="question-header">
                        <h2>What is your business located? <span style={{ color: "red" }}>*</span></h2>
                    </div> */}

                    <div>
                        {validationErrors.address ? (<p className="errors">{validationErrors.address}</p>) : null}

                        <input type="text"
                            value={address}
                            placeholder="Business Address"
                            onChange={e => setAddress(e.target.value)}
                        />
                    </div>
                </div>
                <div className="input-select">
                    {/* <div className="question-header">
                        <h2>What phone number can customer's contact your business? <span style={{ color: "red" }}>*</span></h2>
                    </div> */}
                    <div className="input-phone">
                        {validationErrors.phone_number ? (<p className="errors">{validationErrors.phone_number}</p>) : null}

                        <input type="text"
                            value={phone_number}
                            placeholder="Business Phone"
                            onChange={e => setPhone_number(e.target.value)}
                        />
                    </div>

                    {/* <div className="question-header">


                        <h2>What is your business' cuisine type? <span style={{ color: "red" }}>*</span></h2>
                    </div> */}
                    <div className="select-cuisine">
                        {validationErrors.cuisine_type ? (<p className="errors">{validationErrors.cuisine_type}</p>) : null}

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

                </div>
                <div>
                    {/* <div className="question-header">
                        <h2>Set your business' operating hours <span style={{ color: "red" }}>*</span></h2>
                    </div> */}
                    <div className="business-hours-input">
                        <div>

                            <h3>Opening time</h3>
                            {validationErrors.opening_time ? (<p className="errors">{validationErrors.opening_time}</p>) : null}
                            <input
                                type="time"
                                value={opening_time}
                                placeholder="Opening time"
                                onChange={e => setOpening_time(e.target.value)}
                            />
                        </div>
                        <div>
                            <h3>Closing time</h3>
                            {validationErrors.closing_time ? (<p className="errors">{validationErrors.closing_time}</p>) : null}

                            <input
                                type="time"
                                value={closing_time}
                                placeholder="Closing time"
                                onChange={e => setClosing_time(e.target.value)}
                            />
                        </div>
                    </div>
                </div>
                <div>
                    <h2>Set your business' image and banner</h2>
                    <div>
                        <div>
                            {/* <span>Business Image</span> */}
                            <input
                                type="text"
                                value={image}
                                placeholder="Business Image"

                                onChange={e => setImage(e.target.value)} />
                        </div>
                        <div>
                            {/* <span>Business Banner</span> */}
                            <input
                                type="text"
                                value={header_image}
                                placeholder="Banner Image"

                                onChange={e => setHeader_image(e.target.value)} />
                        </div>
                    </div>
                </div>
                {/* <div id="mini-preview">
                    <div className="business-preview">
                        <h8>{name}</h8>
                        <img className="mini-image" src={image} />
                    </div>
                </div> */}
                <div>
                    <button className="btn " type="submit">Submit</button>
                </div>
            </form>
        </div>

    )
}

export default RestaurantForm
