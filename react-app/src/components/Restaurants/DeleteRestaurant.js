import { useHistory } from "react-router-dom";
import { useDispatch } from 'react-redux';
import { useModal } from "../../context/Modal";
import { thunkDeleteRestaurant, thunkUserRestaurants } from '../../store/restaurant'
import "./DeleteRestaurant.css"

const DeleteRestaurant = ({ restaurant }) => {
    const history = useHistory()
    const dispatch = useDispatch()
    const { closeModal } = useModal()

    const handleDelete = async (e) => {
        e.preventDefault()

        await dispatch(thunkDeleteRestaurant(restaurant))
        dispatch(thunkUserRestaurants())
        .then(closeModal)
    }

    return (
        <div>
            <div>
                <h1>Are you sure you want to delete this Restaurant?</h1>
            </div>
            <div className="delete-btns">
                <button onClick={handleDelete}>Delete Restaurant</button>
                <button className="cancel" onClick={closeModal}>Cancel</button>
            </div>
        </div>
    )

}

export default DeleteRestaurant
