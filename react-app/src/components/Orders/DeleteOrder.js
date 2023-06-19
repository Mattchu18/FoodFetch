import { useDispatch, useSelector } from "react-redux"
import { useModal } from "../../context/Modal";
import { thunkDeleteOrder, thunkUserOrders } from "../../store/order"


const DeleteOrder = ({ order }) => {
    const dispatch = useDispatch()
    const { closeModal } = useModal()

    const handleDelete = async (e) => {
        e.preventDefault()

        await dispatch(thunkDeleteOrder(order))
        dispatch(thunkUserOrders())
        .then(closeModal)
    }

    return (
        <>
        <div>
            <h1>Are you sure you want to cancel this Order?</h1>
        </div>
        <div>
            <button onClick={handleDelete}>Cancel Order</button>
            <button onClick={closeModal}>Take Me Back!</button>
        </div>
    </>

    )
}

export default DeleteOrder
