import { useModal } from "../../context/Modal"
import { useEffect, useState } from 'react'
import { thunkUserOrders } from "../../store/order"
import { useDispatch, useSelector } from "react-redux"

const ViewOrder = ({ order, order_dish }) => {


    return (
        <div>
            <p>Order #{order.id}</p>
            <br />

            <br />
            <p>Order total: ${order.total_amount}</p>
            <p>Order placed: {order.created_at}</p>
            <p>Pick up time: {order.pick_up}</p>
        </div>

    )
}

export default ViewOrder
