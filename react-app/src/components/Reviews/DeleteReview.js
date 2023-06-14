import { useHistory } from "react-router-dom";
import { useDispatch } from 'react-redux';
import { useModal } from "../../context/Modal";
import { thunkDeleteReview, thunkUserReviews } from '../../store/review'


const DeleteReview = ({ review }) => {
    const dispatch = useDispatch()
    const history = useHistory()
    const { closeModal } = useModal()

    const handleDelete = () => {
        dispatch(thunkDeleteReview)
            .then(closeModal)
        dispatch(thunkUserReviews())
        console.log("DELETED!!")
    }

    return (
        <>
            <div>
                <h1>Are you sure you want to delete this Review?</h1>
            </div>
            <div>
                <button onClick={handleDelete}>Delete</button>
                <button onClick={closeModal}>Cancel</button>
            </div>
        </>
    )
}

export default DeleteReview
