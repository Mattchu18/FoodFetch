import { useHistory } from "react-router-dom";
import { useDispatch } from 'react-redux';
import { useModal } from "../../context/Modal";
import { thunkDeleteReview, thunkUserReviews, thunkAllReviews } from '../../store/review'
import "./DeleteReview.css"

const DeleteReview = ({ review }) => {
    const dispatch = useDispatch()
    const history = useHistory()
    const { closeModal } = useModal()

    const handleDelete = async (e) => {
        await dispatch(thunkDeleteReview(review))
        dispatch(thunkUserReviews())
        dispatch(thunkAllReviews())
        .then(closeModal)

    }

    return (
        <div>
            <div>
                <h1>Are you sure you want to delete this Review?</h1>
            </div>
            <div className="handle-delete">
                <button onClick={handleDelete}>Delete</button>
                <button className="cancel-delete" onClick={closeModal}>Cancel</button>
            </div>
        </div>
    )
}

export default DeleteReview
