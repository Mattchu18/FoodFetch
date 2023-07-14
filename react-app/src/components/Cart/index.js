import { useEffect } from "react"
import { thunkUserOrderDishes } from "../../store/order_dish"
import { useDispatch, useSelector } from "react-redux"

const Cart = () => {
    const dispatch = useDispatch()
    const userOrderDishesObj = useSelector(state => state.orderDish.currentUserOrderDishes)
    const userOrderDish = Object.values(userOrderDishesObj)


    useEffect(() => {
        dispatch(thunkUserOrderDishes())

    }, [dispatch])

    return (

        <>
            {userOrderDish.map(item => (
                <>
                    <span>Cart item {item.id}</span>
                    <span>quantity:{item.quantity}</span>
                    <br/>
                </>
            ))}
        </>

    )
}

export default Cart
