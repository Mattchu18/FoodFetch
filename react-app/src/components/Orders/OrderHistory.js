import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import { thunkUserOrders } from "../../store/order"
import { thunkUserRestaurants } from "../../store/restaurant"
import { thunkUserReviews } from "../../store/review"
import { Link } from "react-router-dom"

const OrderHistory = () => {
    const dispatch = useDispatch()
    const userOrdersObj = useSelector(state => state.order.currentUserOrders)
    const userOrders = Object.values(userOrdersObj)
    console.log("this is userOrders =======>", userOrders)

    useEffect(() => {
        dispatch(thunkUserOrders())
    }, [dispatch])

    return (
        <div id="order-history-center">
            <div id="order-history-container">
                <h1>
                    Order History
                </h1>
                <div>
                    {userOrders.map(order => (
                        <div>
                            <div>
                                <h2>Order #{order.id}</h2>
                            </div>
                            <div>
                                <span>Pickup time {order.pick_up}</span>
                            </div>
                        </div>

                    ))}

                </div>
            </div>

        </div>
    )
}

export default OrderHistory
