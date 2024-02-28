// Filename - Home.js


import { Outlet, Link } from "react-router-dom";

const Home = () => {
  return (
    <>
      <nav>
        <ul>
          <li>
            <Link to="stats">Stats</Link>
          </li>
          <li>
            <Link to="maps">Maps</Link>
          </li>
        </ul>
      </nav>

      <Outlet />
    </>
  )
};

export default Home;
