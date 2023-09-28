import { React, useState } from 'react';
import { useDispatch } from 'react-redux';
import { useHistory } from 'react-router-dom';
import { thunkSearchRestaurant } from "../../store/restaurant"

const Search = () => {
    const dispatch = useDispatch()
    const history = useHistory()
    const [query, setQuery] = useState("")


    const handleSubmit = async (e) => {
        e.preventDefault()
        console.log("this is query.trim()====> ", query.trim().length)
        if (query.trim().length > 0) {
            await dispatch(thunkSearchRestaurant(query.trim()))
                .then(history.push("/restaurants/results"))//send to results page
        }
    }

    return (


        <form className='search-bar-container' onSubmit={handleSubmit}>

            <input className="search-bar" type='text' value={query} onChange={e => setQuery(e.target.value)} />
            <button type="submit">Search</button>

        </form>
    )
}

export default Search
