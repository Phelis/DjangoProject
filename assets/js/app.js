import React from 'react';
import axios from 'axios';
import a from './a.css';

class App extends React.Component {

  handleClick() {
    axios.get('create/', {
      Authorization: "Token 5820c8bf171b1a5143e2487e4032c9ebfc8b2dc4"
    }).then(function(response) {
      console.log(response);
      alert(response.data.status);
    });
  }

  showLog() {
    console.log("showLog");
  }

  render() {
    return (
      <div>
        <button type="button" onClick= {this.showLog}>Basic</button>
        Hello {this.props.name}
        Hello {this.props.para}
      </div>
    );
  }
}

export default App;
