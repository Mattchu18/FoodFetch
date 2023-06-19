import { useModal } from "../../context/Modal"
import { useEffect, useState } from 'react'
import { thunkUserOrders } from "../../store/order"
import { useDispatch, useSelector } from "react-redux"

const OneDish = ({ dish, restaurantId }) => {
    const dispatch = useDispatch()
    const ordersObj = useSelector(state => state.order.currentUserOrders)
    const [cartItems, setCartItems] = useState([])
    const [quantity, setQuantity] = useState('')


    useEffect(() =>{
        dispatch(thunkUserOrders())

    }, [dispatch] )
    function addToCart(item) {
        setCartItems(items => [...items, item])

    }

    console.log("this is ordersObj======>", ordersObj)
    return (
        <div>
            <div>
                <h2>{dish.name}</h2>
                <span>{dish.description}</span>
            </div>
            <div>
                <h2>PIC</h2>
            </div>
            <div>
                <div>
                    ${dish.price}
                </div>
                <input type="number" value={quantity} />

                <button onClick={ () => addToCart({"dish_id":dish.id, "quantity":quantity})}>
                    add to cart, restaurantId: {restaurantId}
                </button>
            </div>
        </div>
    )
}


export default OneDish
