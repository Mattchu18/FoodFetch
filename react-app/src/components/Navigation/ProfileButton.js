import React, { useState, useEffect, useRef } from "react";
import { useDispatch } from "react-redux";
import { logout } from "../../store/session";
import OpenModalButton from "../OpenModalButton";
import LoginFormModal from "../LoginFormModal";
import SignupFormModal from "../SignupFormModal";
import { Link, useHistory } from "react-router-dom";

function ProfileButton({ user }) {
  const history = useHistory()
  const dispatch = useDispatch();
  const [showMenu, setShowMenu] = useState(false);
  const ulRef = useRef();

  const openMenu = () => {
    if (showMenu) return;
    setShowMenu(true);
  };


  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = (e) => {
      if (!ulRef.current.contains(e.target)) {
        setShowMenu(false);
      }
    };

    document.addEventListener("click", closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);

  const handleLogout = (e) => {
    e.preventDefault();
    dispatch(logout())
      .then(closeMenu)
    history.push("/")
  };

  const ulClassName = "profile-dropdown" + (showMenu ? "" : " hidden");
  const closeMenu = () => setShowMenu(false);

  return (
    <>
      <button className="bars" onClick={openMenu}>
        <i class="fa-solid fa-bars"></i>
      </button>
      <ul className={ulClassName} ref={ulRef}>
        <div className="x-button-div">
          <button onClick={closeMenu}>X</button>
        </div>
        {user ? (
          <>
            <Link className="menu-links" to="/">
              <div className="menu-link-div">
                <i class="fa-solid fa-house"></i>
                <span>Home</span>
              </div>
            </Link>
            {/* link to account */}
            <div className="menu-links " to="/">
              <div className="menu-link-div account">
                <i class="fa-regular fa-circle-user"></i>
                <span>Account</span>
                <div className="account-info">
                  <strong>Username</strong>
                  <span>{user.username}</span>
                  <br />
                  <strong>Email</strong>
                  <span>{user.email}</span>
                  <br />
                  <strong>Phone</strong>
                  <span>{user.phone_number}</span>
                </div>

              </div>
            </div>
            <div className="menu-links" to="/orders">
              <div className="menu-link-div">
                <i class="fa-solid fa-receipt"></i>
                <span>Orders</span> <span><strong>Coming soon!!</strong></span>

              </div>
            </div>
            {/* <Link className="menu-links" to="/orders">
              <div className="menu-link-div">
                <i class="fa-solid fa-receipt"></i>
                  <span>Orders</span>

              </div>
            </Link> */}

            {user.restaurant_owner === true ? (<Link className="menu-links" to="/restaurants/user">
              <div className="menu-link-div">
                <i class="fa-regular fa-building"></i>

                <span>Your Businesses</span>


              </div>
            </Link>) : null}


            <span className="dropdown-btn">
              <button onClick={handleLogout}>Log Out</button>
            </span>
          </>
        ) : (
          <div className="login-signup-div">
            <div className="dropdown-btn">

              <OpenModalButton
                buttonText="Log In"
                onButtonClick={closeMenu}
                modalComponent={<LoginFormModal />}
              />
            </div>

            <div className="dropdown-btn">
              <OpenModalButton
                buttonText="Sign Up"
                onButtonClick={closeMenu}
                modalComponent={<SignupFormModal />}
              />
            </div>
          </div>
        )}
      </ul>
    </>
  );
}

export default ProfileButton;
