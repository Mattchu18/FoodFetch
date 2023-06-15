import { useHistory } from "react-router-dom";
import { useDispatch } from 'react-redux';
import { useModal } from "../../context/Modal";
import { thunkDeleteRestaurant, thunkUserRestaurants } from '../../store/restaurant'


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
        <>
            <div>
                <h1>Are you sure you want to delete this Restaurant?</h1>
            </div>
            <div>
                <button onClick={handleDelete}>Delete</button>
                <button onClick={closeModal}>Cancel</button>
            </div>
        </>
    )

}

export default DeleteRestaurant
