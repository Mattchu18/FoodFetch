const GET_ONE_ORDER_DISH = "order_dish/oneOrderDish"
const GET_ALL_ORDER_DISHES = "order_dish/allOrderDishes"
const GET_USER_ORDER_DISHES = "order_dish/userOrderDishes"
const CREATE_ORDER_DISH = "order_dish/createOrderDish"
const EDIT_ORDER_DISH = "order_dish/editOrderDish"
const DELETE_ORDER_DISH = "order_dish/deleteOrderDish"


const getOneOrderDish = (orderDish) => ({
    type: GET_ONE_ORDER_DISH,
    orderDish
})

const getUserOrderDishes = (orderDishes) => ({
    type: GET_USER_ORDER_DISHES,
    orderDishes
})

const createOrderDish = (orderDish) => ({
    type: CREATE_ORDER_DISH,
    orderDish
})

const editOrderDish = (orderDish) => ({
    type:EDIT_ORDER_DISH,
    orderDish
})

const deleteOrderDish = (orderDish) => ({
    type: DELETE_ORDER_DISH,
    orderDish
})


export const thunkOneOrderDish = (orderDishId) => async (dispatch) => {
    const response = await fetch(`/api/order_dishes/${orderDishId}`)
    if (response.ok) {
        const data = await response.json()
        dispatch(getOneOrderDish(data))
    }
}

export const thunkUserOrderDishes = () => async (dispatch) => {
    const response = await fetch(`/api/order_dishes/user`)
    if (response.ok) {
        const data = await response.json()
        dispatch(getUserOrderDishes(data))
    }
}

export const thunkCreateOrderDish = (dish) => async (dispatch) => {
    const response = await fetch(`/api/dishes/${dish.id}/cart/add`, {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(dish)
    })
    if (response.ok) {
        const data = await response.json()
        dispatch(createOrderDish(data))
    }
}

export const thunkEditOrderDish = (orderDish) => async (dispatch) => {
    const response = await fetch(`/api/order_dishes/${orderDish.id}/edit`, {
        method: "PUT",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(orderDish)
    })
    if (response.ok) {
        const data = await response.json()
        dispatch(editOrderDish(data))
    }
}


export const thunkDeleteOrderDish = (orderDishId) => async (dispatch) => {
    const response = await fetch(`/api/order_dishes/${orderDishId}/delete`, {
        method: "DELETE"
    })
    if (response.ok) {
        const data = await response.json()
        dispatch(deleteOrderDish(data))
    }
}


const initialState = { currentUserOrderDishes: {}, singleOrderDish: {}, allOrderDishes: {} }
const orderDishReducer = (state = initialState, action) => {
    switch(action.type) {
        case GET_ONE_ORDER_DISH: {
            const newState = {}
            const newOrderDish = action.orderDish
            newState[newOrderDish.id] = newOrderDish
            return {
                ...state,
                singleOrderDish: newState
            }
        }
        case GET_ALL_ORDER_DISHES: {
            const newState = {}
            const allOrderDishes = action.orderDishes
            allOrderDishes.forEach(orderDish => {
                newState[orderDish.id] = orderDish
            })
            return {
                ...state,
                allOrderDishes: newState
            }
        }
        case GET_USER_ORDER_DISHES: {
            const newState = {}
            const userOrderDishes = action.orderDishes
            console.log("This user order dishes action ====> ",userOrderDishes)
            userOrderDishes.forEach(orderDish => {
                newState[orderDish.id] = orderDish
            })
            return {
                ...state,
                currentUserOrderDishes: newState
            }
        }
        case CREATE_ORDER_DISH: {
            const newState = {}
            const newOrderDish = action.orderDish
            newState[newOrderDish.id] = newOrderDish
            return {
                ...state,
                singleOrderDish: newState,
                allOrderDishes: { ...state.allOrderDishes, ...newState}
            }
        }
        case EDIT_ORDER_DISH: {
            const newState = {}
            const newOrderDish = action.orderDish
            newState[newOrderDish.id] = newOrderDish
            return {
                currentUserOrderDishes: { ...state.currentUserOrderDishes, ...newState},
                singleOrderDish: newState,
                allOrderDishes: { ...state.allOrderDishes}
            }
        }
        case DELETE_ORDER_DISH: {
            const newState = { ...state.currentUserOrderDishes }
            const newSingleState = { ...state.singleOrderDish }
            const orderDishId = action.orderDish.orderDishId
            delete newState[orderDishId]
            delete newSingleState[orderDishId]
            return {
                currentUserOrderDishes: newState,
                singleOrderDish: newSingleState,
                allOrderDishes: { ...state.allOrderDishes}
            }
        }
        default: return state
    }

}

export default orderDishReducer
