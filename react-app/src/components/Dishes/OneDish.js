import { useModal } from "../../context/Modal"
import { useEffect, useState } from 'react'
import { thunkUserOrders } from "../../store/order"
import { useDispatch, useSelector } from "react-redux"
import EditDish from "./EditDish"
import DeleteDish from "./DeleteDish"
import './OneDish.css'
import OpenModalButton from "../OpenModalButton"

const OneDish = ({ dish, restaurantId }) => {
    const dispatch = useDispatch()
    const { closeModal } = useModal();
    const ordersObj = useSelector(state => state.order.currentUserOrders)
    const [cartItems, setCartItems] = useState([])
    const [quantity, setQuantity] = useState('')


    useEffect(() => {
        dispatch(thunkUserOrders())

    }, [dispatch])


    return (
        <div id="one-dish-modal">
            <div className="one-dish-header">
                <h1>{dish.name}</h1>
                <button onClick={closeModal} className="close-modal-btn"><strong>X</strong></button>

                <OpenModalButton
                    buttonText="Update your entree"
                    modalComponent={<EditDish
                        dish={dish}
                        restaurantId={restaurantId}
                    />}
                />
                <OpenModalButton
                    buttonText="Delete your entree"
                    modalComponent={<DeleteDish
                        dish={dish}
                        restaurantId={restaurantId}
                    />}
                />
            </div>
            <div className="dish-price">
                <h3>${dish.price}</h3>
            </div>
            <div className="dish-description">
                <span >{dish.description}</span>
            </div>
            <div className="dish-image">
                <img src={dish.dish_image} />
            </div>

        </div>
    )
}


export default OneDish
