const GET_ONE_ORDER = "order/oneOrder"
const GET_ALL_ORDERS = "order/allOrders"
const GET_USER_ORDERS = "order/userOrders"
const CREATE_ORDER = "order/createOrder"
const EDIT_ORDER = "order/editOrder"
const DELETE_ORDER = "order/deleteOrder"


const getOneOrder = (order) => ({
    type: GET_ONE_ORDER,
    order
})

const getAllOrders = (orders) => ({
    type: GET_ALL_ORDERS,
    orders
})

const getUserOrders = (orders) => ({
    type: GET_USER_ORDERS,
    orders
})

const createOrder = (order) => ({
    type: CREATE_ORDER,
    order
})

const editOrder = (order) => ({
    type: EDIT_ORDER,
    order
})

const deleteOrder = (order) => ({
    type: DELETE_ORDER,
    order
})


export const thunkOneOrder = (orderId) => async (dispatch) => {
    const response = await fetch(`/api/orders/${orderId}`)
    if (response.ok) {
        const data = await response.json()
        dispatch(getOneOrder(data))
    }
}

export const thunkAllOrders = () => async (dispatch) => {
    const response = await fetch('/api/orders')
    if (response.ok) {
        const data = await response.json()
        dispatch(getAllOrders(data))
    }
}

export const thunkUserOrders = () => async (dispatch) => {
    const response = await fetch('/api/orders/user')
    if (response.ok) {
        const data = await response.json()
        dispatch(getUserOrders(data))
    }
}

export const thunkCreateOrder = (order) => async (dispatch) => {
    const response = await fetch('/api/restaurants/orders', {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(order)
    })
    if (response.ok) {
        const data = await response.json()
        dispatch(createOrder(data))
    }
}

export const thunkEditOrder = (order) => async (dispatch) => {
    const response = await fetch(`/api/orders/${order.id}/edit`, {
        method: "PUT",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(order)
    })
    if (response.ok) {
        const data = await response.json()
        dispatch(editOrder(data))
    }
}

export const thunkDeleteOrder = (order) => async (dispatch) => {
    const response = await fetch (`/api/orders/${order.id}/delete`, {
        method: "DELETE"
    })
    if (response.ok) {
        const data = await response.json()
        dispatch(deleteOrder(data))
    }
}


const initialState = { currentUserOrders: {}, singleOrder: {}, allOrders: {} }
const orderReducer = (state = initialState , action) => {
    switch(action.type) {
        case GET_ONE_ORDER: {
            const newState = {}
            const newOrder = action.order
            newState[newOrder.id] = newOrder
            return {
                ...state,
                singleOrder: newState
            }
        }
        case GET_ALL_ORDERS: {
            const newState = {}
            const allOrders = action.orders
            allOrders.forEach(order => {
                newState[order.id] = order
            })
            return {
                ...state,
                allOrders: newState
            }
        }
        case GET_USER_ORDERS: {
            const newState = {}
            const userOrders = action.orders
            userOrders.forEach(order => {
                newState[order.id] = order
            })
            return {
                ...state,
                currentUserOrders: newState
            }
        }
        case CREATE_ORDER: {
            const newState = {}
            const newOrder = action.order
            newState[newOrder.id] = newOrder
            return {
                ...state,
                singleOrder: newState,
                allOrders: { ...state.allOrders, ...newState }
            }
        }
        case EDIT_ORDER: {
            const newState = {}
            const newOrder = action.order
            newState[newOrder.id] = newOrder
            return {
                currentUserOrders: { ...state.currentUserOrders, ...newState },
                singleOrder: newState,
                allOrders: { ...state.allOrders }
            }
        }
        case DELETE_ORDER: {
            const newState = { ...state.currentUserOrders  }
            const newSingleState = { ...state.singleOrder }
            const orderId = action.order.orderId
            delete newState[orderId]
            delete newSingleState[orderId]
            return {
                currentUserOrders: newState,
                singleOrder: newSingleState,
                allOrders: { ...state.allOrders }
            }
        }
        default: return state
    }

}

export default orderReducer
