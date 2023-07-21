import { useHistory } from "react-router-dom";
import { useDispatch } from 'react-redux';
import { useModal } from "../../context/Modal";
import { thunkAllRestaurantDishes, thunkDeleteDish } from '../../store/dish'

const DeleteDish = ({ dish, restaurantId }) => {
    const dispatch = useDispatch()
    const { closeModal } = useModal()

    const handleDelete = async (e) => {
        e.preventDefault()

        await dispatch(thunkDeleteDish(dish, restaurantId))
        dispatch(thunkAllRestaurantDishes(restaurantId))
        .then(closeModal)
    }

    return (
        <div>
            <div>
                <h1>Are you sure you want to delete this Entree?</h1>
            </div>
            <div className="delete-btns">
                <button onClick={handleDelete}>Delete Entree</button>
                <button className="cancel" onClick={closeModal}>Cancel</button>
            </div>
        </div>

    )
}

export default DeleteDish
