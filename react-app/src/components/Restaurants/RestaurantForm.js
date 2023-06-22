import { useDispatch } from "react-redux";
import { useEffect, useState } from "react";
import { useHistory } from "react-router-dom";
import { thunkCreateRestaurant, thunkEditRestaurant } from "../../store/restaurant";
import { useModal } from "../../context/Modal";
import './RestaurantForm.css'

const endsWith = (url) => !url.endsWith(".jpg") && !url.endsWith(".png") && !url.endsWith(".jpeg") && !url.endsWith(".webp")

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

        console.log(typeof phone_number)
        if (name.length > 200) errors.name = "Name must be less than 200 characters"
        if (name.length < 2) errors.name = "Name must be more than 2 characters"
        if (!name) errors.name = "Name is required"
        if (name.trim().length ===0) errors.name = "Name cannot only be whitespace"
        if (address.length > 200) errors.address = "Address must be less than 200 characters"
        if (!address) errors.address = "Address is required"
        if (address.trim().length ===0) errors.address = "Address cannot only be whitespace"
        if (!phone_number) errors.phone_number = "Phone number is required"
        if (!cuisine_type) errors.cuisine_type = "Cuisine type is required"
        if (!opening_time) errors.opening_time = "Opening time is required"
        if (!closing_time) errors.closing_time = "Closing time is required"
        if(image.length > 1000) errors.image = "Image url must be less than 1000 characters long"
        // if (image.trim().length ===0) errors.image = "Image url cannot only be whitespace"
        if (image.length && endsWith(image)) errors.image = "Image URL must end in .png, .jpg, or .webp or .jpeg"
        if(header_image.length > 1000) errors.header_image = "Header Image url must be less than 1000 characters long"
        if (header_image.length && endsWith(header_image)) errors.header_image = "Header Image URL must end in .png, .jpg, or .webp or .jpeg"
        // if (header_image.trim().length ===0) errors.header_image = "Header Image url cannot only be whitespace"

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
                            placeholder="Business Name  *required"
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
                        {formType === "Create Restaurant" ?
                            (<input type="text"
                                value={address}
                                placeholder="Business Address  *required"
                                onChange={e => setAddress(e.target.value)}
                            />) : null
                        }


                    </div>
                </div>
                <div className="input-select">
                    {/* <div className="question-header">
                        <h2>What phone number can customer's contact your business? <span style={{ color: "red" }}>*</span></h2>
                    </div> */}
                    <div className="input-phone">
                        {validationErrors.phone_number ? (<p className="errors">{validationErrors.phone_number}</p>) : null}

                        <input type="tel"
                            maxLength="12"
                            minLength="12"
                            pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}"
                            value={phone_number}
                            placeholder="ex: 123-456-7890  *required"
                            onChange={e => setPhone_number(e.target.value)}
                        />
                    </div>

                    {/* <div className="question-header">


                        <h2>What is your business' cuisine type? <span style={{ color: "red" }}>*</span></h2>
                    </div> */}
                    <div className="select-cuisine">
                        {validationErrors.cuisine_type ? (<p className="errors">{validationErrors.cuisine_type}</p>) : null}
                        {formType === "Create Restaurant" ? (<select onChange={e => setCuisine_type(e.target.value)} value={cuisine_type}>
                            <option value="">Cuisine  *required</option>
                            <option value="Burgers">Burgers</option>
                            <option value="Filipino">Filipino</option>
                            <option value="Chinese">Chinese</option>
                            <option value="Pizza">Pizza</option>
                            <option value="Boba">Boba</option>
                            <option value="Mediterranean">Mediterranean</option>
                            <option value="Vietnamese">Vietnamese</option>
                            <option value="Sushi">Sushi</option>
                            <option value="Coffee">Coffee</option>
                            <option value="Chicken">Chicken</option>
                            <option value="Korean">Korean</option>
                        </select>) : null}

                    </div>

                </div>
                <div>
                    {/* <div className="question-header">
                        <h2>Set your business' operating hours <span style={{ color: "red" }}>*</span></h2>
                    </div> */}
                    <div className="business-hours-input">
                        <div>

                            <h3>Opening time</h3>
                            <p>* required</p>
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
                            <p>* required</p>
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
                    <div>
                        <h3>Business image</h3>
                        <div>
                        {validationErrors.image ? (<p className="errors">{validationErrors.image}</p>) : null}

                            {/* <span>Business Image</span> */}
                            <input
                                type="text"
                                value={image}
                                placeholder="Business Image (optional)"
                                onChange={e => setImage(e.target.value)} />
                        </div>
                        <h3>Business banner</h3>
                        <div>
                        {validationErrors.header_image ? (<p className="errors">{validationErrors.header_image}</p>) : null}

                            {/* <span>Business Banner</span> */}
                            <input
                                type="text"
                                value={header_image}
                                placeholder="Banner Image (optional)"

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
