import { useDispatch } from "react-redux";
import { useEffect, useState } from "react";
import { useHistory } from "react-router-dom";
import { thunkAllRestaurantDishes, thunkCreateDish } from "../../store/dish";
import { useModal } from "../../context/Modal";

const DishForm = ({ dish, restaurantId, formType }) => {
    const dispatch = useDispatch()
    const history = useHistory()
    const { closeModal } = useModal()

    const [name, setName] = useState(dish?.name)
    const [description, setDescription] = useState(dish?.description)
    const [price, setPrice] = useState(dish?.price)
    const [dish_image, setDish_Image] = useState(dish?.dish_image || "")
    const [validationErrors, setValidationErrors] = useState("")

    const handleSubmit = async (e) => {
        e.preventDefault()

        const formData = new FormData()

        formData.append("name", name)
        formData.append("description", description)
        formData.append("price", price)
        formData.append("dish_image", dish_image)

        let errors = {}
        if (!name) errors.name = "Dish name is required"
        if (!description) errors.description = "Dish description is required"
        if (!price) errors.price = "Dish rice is required"
        if (!dish_image) errors.dish_image = "Dish image is required"

        setValidationErrors(errors)

        if (formType === "Create Dish" && !Object.keys(errors).length) {
            await dispatch(thunkCreateDish(formData, restaurantId))
            dispatch(thunkAllRestaurantDishes(restaurantId))
                .then(closeModal)
        }
        // if (formType === "Edit Dish" && !Object.keys(errors).length) {

        //     await dispatch(thunkEditDish(formData, dish))
        //         .then(closeModal)
        // }

        if (!!Object.keys(errors).length) return
    }

    return (
        <div id="create-restaurant-form">
            <form
                onSubmit={handleSubmit}
                encType="multipart/form-data"
            >
                <div>
                    {formType === "Create Dish" ? (<h1>Create your dish!</h1>) : (<h1>Update your dish!</h1>)}
                </div>
                <div>
                    <div>

                        {validationErrors.name ? (<p className="errors">{validationErrors.name}</p>) : null}
                        <input type="text"
                            value={name}
                            placeholder="* Dish Name"
                            onChange={e => setName(e.target.value)}

                        />
                    </div>
                </div>
                <div>
                    <div>
                        {validationErrors.description ? (<p className="errors">{validationErrors.desciption}</p>) : null}
                        {(<input type="textarea"
                            value={description}
                            placeholder="* Dish Description"
                            onChange={e => setDescription(e.target.value)}
                        />)}
                    </div>
                </div>
                <div className="input-select">
                    {/* <div className="question-header">
                        <h2>What phone number can customer's contact your business? <span style={{ color: "red" }}>*</span></h2>
                    </div> */}
                    <div className="input-phone">
                        {validationErrors.price ? (<p className="errors">{validationErrors.price}</p>) : null}

                        <input type="number"
                            step="0.01"
                            min="0"
                            value={price}
                            placeholder="* Dish Price"
                            onChange={e => setPrice(e.target.value)}
                        />
                    </div>

                </div>
                <div>
                    <div>
                        <h3>Dish image</h3>
                        <div>
                            {validationErrors.dish_image ? (<p className="errors">{validationErrors.dish_image}</p>) : null}
                            <input
                                type="file"
                                accept="image/*"
                                placeholder="Dish Image"
                                onChange={e => setDish_Image(e.target.files[0])} />
                        </div>
                    </div>
                </div>
                <div className="required-field"><label>* Required field</label></div>
                <div>
                    <button className="btn " type="submit">Submit</button>
                </div>
            </form>
        </div>


    )
}

export default DishForm
