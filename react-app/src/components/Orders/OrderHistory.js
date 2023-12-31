import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import { thunkUserOrders } from "../../store/order"
import { thunkAllRestaurants } from "../../store/restaurant"
import { thunkUserReviews } from "../../store/review"
import { thunkUserOrderDishes } from "../../store/order_dish"
import { thunkAllDishes } from "../../store/dish"
import { Link } from "react-router-dom"
import OpenModalButton from "../OpenModalButton"
import DeleteOrder from "./DeleteOrder"
import ViewOrder from "./ViewOrderModal"

import './OrderHistory.css'


const OrderHistory = () => {
    const dispatch = useDispatch()
    const user = useSelector(state => state.session.user)

    const userOrdersObj = useSelector(state => state.order.currentUserOrders)
    const userOrders = Object.values(userOrdersObj)

    const restaurantsObj = useSelector(state => state.restaurant.allRestaurants)
    const restaurants = Object.values(restaurantsObj)

    const userOrderDishesObj = useSelector(state => state.orderDish.currentUserOrderDishes)
    const userOrderDishes = Object.values(userOrderDishesObj)

    const allDishesObj = useSelector(state => state.dish.allDishes)
    const allDishes = Object.values(allDishesObj)



    userOrders.forEach(order => {
        const filteredRestaurants = restaurants.filter(restaurant => restaurant.id == order.restaurant_id)
        filteredRestaurants.forEach(restaurant => {
            order["restaurantName"] = restaurant.name
            order["restaurantAddress"] = restaurant.address
            order["restaurantImage"] = restaurant.image
            // userOrdersArr.push(order)
        })
    })


    useEffect(() => {
        dispatch(thunkUserOrders())
        dispatch(thunkAllRestaurants())
        dispatch(thunkUserOrderDishes())
        dispatch(thunkAllDishes())
    }, [dispatch])


    if (!user) return "Please log in to view this feature"
    if (!userOrders || !Array.isArray(userOrders)) return null;
    if (!userOrderDishes || !Array.isArray(userOrderDishes)) return null;
    if (!allDishes || !Array.isArray(allDishes)) return null;
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
                            <Link to={`/restaurants/${order.restaurant_id}`}>

                                <div className="order-restaurant-image">
                                    <img src={order.restaurantImage}
                                        onError={e => { e.currentTarget.src = "https://cdn.discordapp.com/attachments/1119886170579550301/1119886247956054026/image-coming-soon.png"; }} />

                                </div>
                            </Link>
                            <div className="restaurant-order-details">

                                <div>
                                    <span>Order #{order.id}</span>
                                </div>
                                <Link to={`/restaurants/${order.restaurant_id}`}>
                                    <h2>{order.restaurantName}</h2>
                                </Link>

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

                                <span>${order.total_amount}</span>
                                <OpenModalButton
                                    buttonText="View Order "
                                    modalComponent={<ViewOrder order={order}
                                        order_dish={userOrderDishes} />}
                                />

                                {order.time_difference ? (<span>Orders cannot be altered after 5 minutes</span>) : null}
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
