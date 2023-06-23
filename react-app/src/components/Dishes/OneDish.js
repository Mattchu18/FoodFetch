import { useModal } from "../../context/Modal"
import { useEffect, useState } from 'react'
import { thunkUserOrders } from "../../store/order"
import { useDispatch, useSelector } from "react-redux"

const OneDish = ({ dish, restaurantId }) => {
    const dispatch = useDispatch()
    const ordersObj = useSelector(state => state.order.currentUserOrders)
    const [cartItems, setCartItems] = useState([])
    const [quantity, setQuantity] = useState('')


    useEffect(() => {
        dispatch(thunkUserOrders())

    }, [dispatch])
    function addToCart(item) {
        setCartItems(items => [...items, item])

    }

    console.log("this is onedish======>", dish)
    return (
        <div id="one-dish-modal">
            <div className="one-dish-header">
                <h1>{dish.name}</h1>
                <span className="dish-description">{dish.description}</span>
            </div>
            <div className="dish-image">
                <img src={dish.dish_image} />
            </div>
            <div>
                <div>
                    ${dish.price}
                </div>
                <input type="number" value={quantity} />

                <button onClick={() => addToCart({ "dish_id": dish.id, "quantity": quantity })}>
                    add to cart, restaurantId: {restaurantId}
                </button>
            </div>
        </div>
    )
}


export default OneDish
