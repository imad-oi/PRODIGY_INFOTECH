'use client';

import NavLink from './NavLink';

export default function Hero() {
  return (
    <section>
      <div className="custom-screen pt-28 text-gray-600">
        <div className="space-y-5 max-w-4xl mx-auto text-center">
          <h1 className="text-4xl text-gray-800 font-extrabold mx-auto sm:text-6xl">
            Predict Your House Price with Machine Learning
          </h1>
          <p className="max-w-xl mx-auto">
            Predict your house price with machine learning. This project uses
            machine learning to predict house prices based on the features of
            the house.

            <br />
          </p>
          <p className='mt-4'>
            It is just a simple project to show how machine learning can be used
          </p>
          <div className="flex items-center justify-center gap-x-3 font-medium text-sm">
            <NavLink
              href="/start"
              className="text-white bg-gray-800 hover:bg-gray-600 active:bg-gray-900 "
            >
              Predict House Price
            </NavLink>
            <NavLink
              target="_blank"
              href="https://github.com/imad-oi/PRODIGY_INFOTECH"
              className="text-gray-700 border hover:bg-gray-50"
              scroll={false}
            >
              Learn more
            </NavLink>
          </div>
          
        </div>
      </div>
    </section>
  );
}
