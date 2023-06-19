import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import { thunkUserOrders } from "../../store/order"
import { thunkAllRestaurants } from "../../store/restaurant"
import { thunkUserReviews } from "../../store/review"
import { Link } from "react-router-dom"
import OpenModalButton from "../OpenModalButton"
import DeleteOrder from "./DeleteOrder"

import './OrderHistory.css'


const OrderHistory = () => {
    const dispatch = useDispatch()
    const userOrdersObj = useSelector(state => state.order.currentUserOrders)
    const userOrders = Object.values(userOrdersObj)
    const restaurantsObj = useSelector(state => state.restaurant.allRestaurants)
    const restaurants = Object.values(restaurantsObj)
    console.log("This is old userOrders=====>", userOrders)

    // const userOrdersArr = []
    userOrders.forEach(order => {
        const filteredRestaurants = restaurants.filter(restaurant => restaurant.id == order.restaurant_id)
        filteredRestaurants.forEach(restaurant => {
            order["restaurantName"] = restaurant.name
            order["restaurantAddress"] = restaurant.address
            order["restaurantImage"] = restaurant.image
            console.log("this is orders!!", order)

            // userOrdersArr.push(order)
        })
    })

    // const pastCancellation =

    console.log("This is new userOrders=====>", userOrders)
    useEffect(() => {
        dispatch(thunkUserOrders())
        dispatch(thunkAllRestaurants())
    }, [dispatch])

    return (
        <div id="order-history-center">
            <div id="order-history-container">
                <div className="order-heading">
                    <h1>Order & Pickup Details</h1>
                    <span>Past Orders</span>
                </div>
                <div id="all-user-order-container">
                    {userOrders.map(order => (
                        <div id="order-container">
                            <div className="order-restaurant-image">
                                <img src={order.restaurantImage} />
                            </div>
                            <div className="restaurant-order-details">

                                <div>
                                    <span>Order #{order.id}</span>
                                </div>

                                <h2>{order.restaurantName}</h2>

                                <div>
                                    <span>
                                        Order placed at {order.created_at}
                                    </span>
                                </div>

                                <div>
                                    <span>Pickup </span>
                                    <span>{order.restaurantAddress}</span>
                                </div>
                                <div>
                                    <span>Pickup time {order.pick_up}</span>
                                </div>
                            </div>
                            <div className="order-history-btn">
                                <div>
                                    <span>${order.total_amount}</span>
                                    <button>View Order</button>
                                </div>
                                <OpenModalButton
                                    disabled={order.time_difference || order.edited}
                                    buttonText="Cancel Order"
                                    modalComponent={<DeleteOrder order={order} />}
                                />
                            </div>
                        </div>
                    ))}

                </div>
            </div>

        </div>
    )
}

export default OrderHistory
