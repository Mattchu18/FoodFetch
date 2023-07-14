import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { signUp } from "../../store/session";
import "./SignupForm.css";

function SignupFormModal() {
	const dispatch = useDispatch();
	const [email, setEmail] = useState("");
	const [username, setUsername] = useState("");
	const [password, setPassword] = useState("");
	const [confirmPassword, setConfirmPassword] = useState("");
	const [phone_number, setPhone_number] = useState("");
	const [restaurant_owner, setRestaurant_owner] = useState(false);
	const [errors, setErrors] = useState([]);
	const { closeModal } = useModal();

	const handleSubmit = async (e) => {
		e.preventDefault();
		if (password === confirmPassword) {
			const data = await dispatch(signUp(username, email, phone_number,
				restaurant_owner, password));
			if (data) {


				setErrors(data);
			} else {
				closeModal();
			}
		} else {
			setErrors([
				"password: Confirm Password field must be the same as the Password field",
			]);
		}
	};

	return (
		<div id="sign-up-modal">
			<h1>Sign Up</h1>
			<form onSubmit={handleSubmit}>
				<ul>
					{errors?.map((error, idx) => (
						<p className="errors" key={idx}>{error}</p>
					))}
				</ul>
				<label>
					Email <span className="required">* required</span>
					<input
						type="text"
						value={email}
						onChange={(e) => setEmail(e.target.value)}
						required
					/>
				</label>
				<label>
					Username <span className="required">* required</span>
					<input
						type="text"
						value={username}
						onChange={(e) => setUsername(e.target.value)}
						required
					/>
				</label>
				<label>
					Phone Number <span className="required">* required</span>
					<input type="tel"
						maxLength="12"
						minLength="12"
						pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}"
						value={phone_number}
						placeholder="ex: 123-456-7890"
						onChange={e => setPhone_number(e.target.value)}
					/>
				</label>
				<div className="owner"><span>Are you a Restaurant Owner?  (optional)</span>
					<input
						type="checkbox"
						value={true}
						onChange={(e) => setRestaurant_owner(e.target.value)}
					>
					</input>
				</div>

				<label>
					Password <span className="required">* required</span>
					<input
						type="password"
						value={password}
						onChange={(e) => setPassword(e.target.value)}
						required
					/>
				</label>
				<label>
					Confirm Password <span className="required">* required</span>
					<input
						type="password"
						value={confirmPassword}
						onChange={(e) => setConfirmPassword(e.target.value)}
						required
					/>
				</label>
				<div className="signup-btn">

					<button type="submit">Sign Up</button>
				</div>
			</form>
		</div>
	);
}

export default SignupFormModal;
