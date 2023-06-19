import OrderForm from "./OrderForm";


const EditOrder = ({ order }) => {

    return (
        <OrderForm
        order = {order}
        formType="Edit Order"
        />
    )
}

export default EditOrder
