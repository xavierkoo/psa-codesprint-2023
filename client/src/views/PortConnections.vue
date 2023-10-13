<template>
  <div class="container-fluid p-0">
    <div
      class="bannerImage"
      style="
        background-image: url('https://img.freepik.com/premium-vector/drawing-boat-port-vietnam-hoi_252525-41.jpg');
      "
    ></div>
    <!-- User Input Form -->
    <div class="row my-4">
      <div class="" v-if="!submitted || loading">
        <div>
          <div class="mb-4 mx-4">
            <h1 class="my-4 text-center">PortConnections</h1>
            <h6 class="fst-italic mb-3 text-center">
              Bridging Teams, Building Relations
            </h6>
            <div class="card-body">
              <form @submit.prevent="submitPreferences">
                <div class="mb-3">
                  <label for="place" class="form-label"
                    >Type of Activities</label
                  >
                  <select v-model="placeType" class="form-select" id="place">
                    <option value="Outdoor">Outdoor</option>
                    <option value="Indoor">Indoor</option>
                  </select>
                </div>
                <div class="mb-3">
                  <label for="NumPeople" class="form-label"
                    >Number of people</label
                  >
                  <select
                    v-model="numPeople"
                    class="form-select"
                    id="NumPeople"
                  >
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                  </select>
                </div>
                <!--Minimum and maximum budget-->
                <div class="row">
                  <div class="col-md-6">
                    <div class="mb-3">
                      <label for="minimum" class="form-label"
                        >Minimum Budget</label
                      >
                      <input
                        v-model="minimum"
                        type="number"
                        class="form-control"
                        id="minimum"
                        placeholder=""
                      />
                    </div>
                  </div>
                  <div class="col-md-6">
                    <div class="mb-3">
                      <label for="maximum" class="form-label"
                        >Maximum Budget</label
                      >
                      <input
                        v-model="maximum"
                        type="number"
                        class="form-control"
                        id="maximum"
                        placeholder=""
                      />
                    </div>
                  </div>
                </div>
                <div class="text-center" v-if="!submitted && !loading">
                  <button type="submit" class="defaultBtn w-50">Submit</button>
                </div>
                <div v-if="submitted && loading" class="my-3"><loader /></div>
              </form>
            </div>
          </div>
        </div>
      </div>
      <!-- Buddy matched -->
      <div class="mx-4" v-if="submitted && displayUsers && !loading">
        <div class="card">
          <div class="card-body text-center">
            <h2 class="card-title">Matched Buddies</h2>
            <!-- Display buddy's name and profile picture -->
            <div class="row text-center">
              <div
                v-for="(user, index) in displayUsers"
                :key="index"
                :class="{
                  'col-md-6': displayUsers.length === 2,
                  'col-md-4': displayUsers.length === 3,
                  'col-12': displayUsers.length === 1,
                }"
              >
                <div class="user-card text-center">
                  <img :src="user.src" alt="User Image" />
                  <h3>{{ user.name }}</h3>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="mx-4" v-if="submitted && !loading">
        <!-- Activities -->
        <div class="row my-3">
          <div
            class="col-6"
            v-for="(activity, index) in groupActivities"
            :key="index"
          >
            <div class="card mb-3">
              <h3 class="card-header">{{ activity.name }}</h3>
              <div class="card-body" style="height: 30%">
                <div class="mb-3">
                  <div class="mb-1">
                    <h6 class="fw-bold d-inline">Location: &nbsp;</h6>
                    {{ activity.location }}
                  </div>
                  <div class="mb-1">
                    <h6 class="fw-bold d-inline">Price range: &nbsp;</h6>
                    {{ activity.price }}
                  </div>
                  <div class="mb-1">
                    <h6 class="fw-bold">Activity information:</h6>
                    {{ activity.description }}
                  </div>
                </div>
                <div class="text-center">
                  <button @click="initiateChatroom" class="defaultBtn">
                    Share with buddies
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import loader from "../components/loader.vue";
const placeType = ref("");
const numPeople = ref("");
const minimum = ref("");
const maximum = ref("");
const submitted = ref(false);
const displayUsers = ref([]);
const groupActivities = ref([]);
const loading = ref(false);

const users = [
  {
    name: "Jason Tan",
    src: "data:image/jpeg;base64,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",
  },
  {
    name: "Isaiah Lee",
    src: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRycbdkZmck1f6zbCTH_KDlDVVjq028IzYwRg&usqp=CAU",
  },
  {
    name: "Alice Sia",
    src: "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHCBIREhISEhISGBgSGBIYERkSEhIYEhgSGBgZGRgYGBgcIS4lHB4tIRgYJzgmKy8xNTU1GiQ7QDs0Py40NTEBDAwMEA8QHBISGjQhJSE0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0MTE0MTQ0NDQ0NDE0NDQ0NDE0NDQ0NDQ0NDQ0NDQ0NP/AABEIAOEA4QMBIgACEQEDEQH/xAAcAAACAgMBAQAAAAAAAAAAAAAAAQIHAwQGBQj/xABFEAACAQICBgcECAQFAgcAAAABAgADEQQhBRIxQVFhBgcTInGBkTKhsfAUI0JScoLB0WKSorJTc8Lh8TRjJCUzNUOz0v/EABgBAQEBAQEAAAAAAAAAAAAAAAABAgME/8QAIREBAQACAgICAwEAAAAAAAAAAAECESExEkEDUTJCkRP/2gAMAwEAAhEDEQA/ALdMUZilURRxQCEIQCEIQCOKOARxRwCYmmWYmgCzKJiBtMNbSNGmdV6tNTwZ1DekDbhNRtI0AoY1aYB2E1FsffJYXHUqt+zqU3tt1HVreNjlA2YQhAIQhAIoQgEIQgKEIGAQhCAzCBigEIQgEIo4BCEIBHFHAI4o4BNbF11pqzuQFUEsTsAE2CZU3TPpMcS7UabfV0yRkc3cfa8OHrBJsulPTqo5anhSUQbX2VGH+ke+cLVeobVH1u9mpZjrN/EZ7uhejlXEvrlDqXubki/nNLpbha1OqRUU6v2DwXh5THlLdOnhZNtKhUZs9bZuv8+hmT6Q9NlenUKuM1ZSVPkRsmhQpHYR+E8OUnSUk6tz57LzbK1Oh3WAHIoYwgNkFqGwU8n3D8Xrxliz5wWgf/yfiDLN6uek5e2Crt3gD9GZtpVRc0yd5AzXlcbs4liw4RQlQQhCAQhCAoQhAIQhAZijMUAihCARxQgOEIQCOKEBwhCBynWHpk4XBlUNnr3ROS277enxnD9CujXb/XVL6gPdG9jvueE2OsPFnE49KCZimEQAffc5/t5SwdG4JaNKnTXYigee+c8q7fHPbLhsKqKAqgAbABNLTGhqeKplHUZ7Ms57KDKDLMadNqQ0/oR8FU1CCVPsNxXgeY/3428l6OsQRt385eWn9Dpi6DU2yO1G3q+4yj9Lo9EtTcar02sw5jbbiN4nTHLfblljO40q+INN7g3H2vDj4j9pt4TGsGSpTbVemyshG51N1PrlPHxL5625rEfr88pDDVbG27L+U/taVh9OaH0guKw9GutrVUVrDcxHeXyNx5TdnD9VGM18E1M7aNRh+V+//cX9J3E0zRCEIChCEAijigO0IQgBijMUIIQihThFHAI4oQHCKOA5jr1QiM52IGY+AFzJzxOl+K7PB1eLgIPzbfdeCK26HH6XparUfPs2qOfxaqKPexlh4hsXrk0zS1RsU3vbx4zh+qSnr1MdW5qo/OzMf7V9067SmialV2btqirqtqKjaq9oR3Sx2kA8Jyy7ejCcNzB6abXFOrSKE7GBup/aeu1UAXM4To7hMehYYpgVudQF9d1sSb69sxbLy3TqdIK3ZqBta0xcrNt+M49I1ukWFU6rVMxwBIld9ZFCjV1MVRYE5JVABBI+y36ek9LS+Nq4RRUp0KZQvqC6O9QtlckKO6Ntr2vqnkDs06zYui9OvhTTaomWV1IZbgg7mF9hzEbsktS4y7kU242rw2fPjea4Nh4HZym1jqD03ZHFmQkHyyM03bfOsee8LY6l8X9biad/bp03/ka3+uW5KG6ocRqaRVb5VKdVfcHH9kviajNOKEJUEIQhRFCEBwhCAjFGYoQQhFCnCEIDhFFAd4XkSYrwJ3nDdZ+M1KNNPxsfTVHxnbXlTda+M+sKX2IB59791Mlax7Z+pmoGpYwbxUpE+an9vdLO1LgXlOdTGLIfG07+0lNwOasyk/1LLapVmItsnPK6rtjzGVlUWA3zHi2AZOUw18Q6sNWmzbywIsOVts86tpRy9nw1UqcldVBUNzF7+dpjK8Nye3sHDg5j/aFSiqjYPQTFga7hLOLW2eG6QxuLFrXk3NGrtVHWRocCoK6ZB7h+GuNh8x8JXjIQcxbxlw9MqfaUgDsLJt5mVv0mrIOyQauuouxW2SnYDbfymvjt1pz+XGb23+rQ6uksPyLe9WH6z6Knz/1aUtfHUGt9og+Sn/aX+J2jhThCKVBCEIURQhAcIoQAwgYoQQhCAQhCFERMDEZQExQigDNYXlCdYON7WtUbi7W/CAFX3AS7tMYrsqFSpwU28Tsnzx0hqazkcCfn3zNax6tZur7SowmPpOxstW9J+SvbVPkwWXtiDUZGFIqHsdQsCVDbiQNonzU1OwseHxl59XPSAYzDhajfXUQq1L7W+6/mB6gzlnPbp8WWuHRYariXUZ0FbMMrM97gG9jbMfvIYirikF2pUio1fZq96xNthE2sTg3N2QgE7b7DPPfBVmI1tUc1za3AG2UzXomr7n8Y9HaTqYioy9jURVHtuF1Cfugg3PjaSegGYsTkOc3Sop0yNlpy2ntP08PTOe4mw2nynO9m3MdaekQKdPDoc3bXa25U2e8j0lcJS1s7kknxueZm1pbHviqrVHObbBuVRsX54yeGSwE9GM1NPJlfLLawuqnBf+KT/tI7nhrHu5+suSV71SYUCjWq2zZwgO+yqCR4ZiWFNxjLsQhFKhxQigEIRQqUIoQAxRmKVBHFCAQhEYAYjGZGFEUJEm0DnOm+J1MORx2+X/IlGYnv1Dvz+PeMtLrFxmync5Lc+JP7/CVfQTMt4+/5WYvbfpp4pO8fX9J1nVST9OqWNvqKh8w9O3xPrOYxK31m8FHlOq6px/5gRxw9X+6nJl0uP5RbqaTdB30NuK5+7bPPx/SymgsNb+UzfejtE1H0MtRsxlPNuvTrFy2N6QV8UezoUz+JvZHMzjulo7JRTL69SpnUY/ZQHYvAE/CWjpypQwFBqjAAAd0C12bcJSOkMU9eo9Wobs5J5DgByAsPKawltZzs000p2mZG2Dj8mYr3ns9FtFnF4qlTGwst/wAOsAfQEnwUzs4Lz6F4H6PgMMlrMya7/ifvfAgeU96QRQAABYAAAcBJTo5HFCEAhFCARQhCpQihADFAwlQ4oQgEIRGAjIxmRMBzRx+lMPROrUrU0bbqtUUPbku038J4XT3pIcDQC0z9dWuEOR1FGRe3HMAc890q3AlmbXZizG7MzElmc/aYnMnfJbprGbr0ul+O7Wo7gmzMbH+EH9rTnkSyDLM525nYPhNzSJ7SpqjYLA+G0+6wmviXCjLbutx+SfWZjdaOOIyRfs7f1nYdT+FLY2rUOxKLKPFnUn+2eX0b6MVcYxIHdHHIeMtzon0dTAoQubPnUa1rnKwA4DP1M55ZempjrmvZKC8w47GJh6bVKjWVQTzPICbddlRdYkZcZU/WF0lDE4embt/8hHsoPuD+LjM6503LxuuX6X9I6mPrXOSKSKaA5AcTxYznXOeWzYPCT4njl5QICi+/O03OGLyx6u71nsdG9O1MDXWtSVGIFitRbqVO3ZmDbeOM8pxqgg/m8eEy4WnlrHfNYzdYyX10Z6a4XHaqXNKqfsVCO8f4H2P4ZHlOmnzWDaddoLrExWF1UrfX0xYWc2qqP4X3+DX8ROjC5oTV0XpGniqKV6TayVBdTsI3EEbiCCCOImzCHFCEAhCKQOEIQAxQaKUShFCAREwiMBEyMCZ5nSLGGhg8TVBsUp1NQn75Fk/qIhVRdM9KfS8dUdc0p2SnzVL2I8Wu3nNegBTQHfmx/QTz0CrY8dnHwmXEYoAamRuO9b+39PWc8ruuuM1EQ9vF+83IbvXb/wATNhcG1atTo0xd6jAAD7K2uT4hQT5TAjFAXfNicubfsJ3fVJovtK1XFuL9mOzpk/4j95z4hbD85mpGLXdaG0KuEDIospYlfwfZF+QnrEZTcInidKNN0tH4dqzgFj3aSXsXfcPAbSdw8pjw+mv9N9uX6wukgwlI0aTXr1RtBzp0z9r8Rtl5nhelajk3NySxOZPqbz0NKYt8RUqVajFnqMSx5nhwG4DcAJpdmPTKPHS7tRRN5+RBQSb87D5+dkzFCLDeRn4R6trnco95tf8AT0hWtqazBeZvN5QAJgpLbzv6SbvadMZqOWV3SqvNctMq0ic28pFgJUWX1PaXIetg2OTL2tIHcykK4HiCht/CZal5QPV9XKaTwhH2ndDzDo6/qD5S/YQ4rxXheA4SN4SCd4RQgBigYpQ4QhARkTGZEmFIzh+tDEMuHoUx7NSr3+eopIB5XN/yidsTKy6ysUXxdGj9mnS1/wA7s1/ci+smXS49q8xWLsxtt2CLC7ydwuTw5+M06o+sa+4mbWH9n3+fz+sxjG7Ww1S+Z4ZclG6X30E0X9FwVGmRZiuu/HtH7xB8AQv5ZSvRzA/ScZhqNrio66w4ovfcfyqZ9GotgBOlc6jWqqiM7sFVAWdmNlCgXJJ4WlA9MukDaQxLVMwiXSgp+yl9pH3m2nyG6dp1q9JLAYCk23VbFEHYNqU/PJjy1eJlWmIsYqh90hhk12F9gz8rgR19k3NF0t5+dtpzrcD0CS55j9cpr4hdUBOJJbytYe8z2GxCgOQPZI91x+88LG1TZm3gX9ds1ImVMG+fHZ4CSCgZnbwkEfIADPK0ncLtzM2wi4J25CYLTJUcnbMYMg6zq0whqaToHdSWpUbwCFB/U6y85XnVBo4Lh6+KIzquET/LQXNvFmP8olhwghFCAQihIJQhCAzFAxXlDhFAwpGQJjJkSYGtj8WlClUq1DZaaszeAGwczs85RdXSb4vF1K9TNqmsbbgMtVRyAyna9ammCOzwaHIgVK3PM6i+oLfyyttFvaofAn3SXpZ2wY5NWo/Mm3gTM1LJRM2kaetnvFx5A2/Sa1I7jtGRkxXJYfVHgu0xr1SMqFNj+dyFX3B5bOmdJJhMPVxD+zSUtb7zbFUcyxA85wnU1QAoYqpbNqipfkiKw/vMxdcWliq0MIpye9WpzCnVQHlfXPiomvbKs8ZiXrVHq1Dd6jM7n+Jjc+XLlIUl1mAtzPlsHwmuz2F5s4RwoJNtnvPz8IqxNsMDcnh8ZNqgp5fN72H6zC+ICBePjv8Am81atQubn8o4AbJnS7M1O6w3uQfMfptmpis1O8n5ymYmYybn58zNIyJwG3fymQADmYqVgMo3OUqMNQnnIIt4OpO+ex0N0OuLx2Ho1LshYtUF8jTRS5U8jqgecguboDhey0bhF3uhc3/7jM49zCdDIgAAAAADIACwAG4QvCHCKKA4RQgTvCRvCQSaEDFeVTkSYyZAmAiZEyRM5/pnpgYTCVGBs9S6UuIZgbt+UXPjbjAqjpnjRXx2KcG6hiindZFCZcrqT5zncM+rUvwF/eJ2uj+r7G1lV2NGmHAIFR2LhTvKqpsbbiR5Tcfqqrggri6J23vTqLYcrE390lyjUxy+nFYmpezDO+/nsPwv5zX19h4/Gev0i6K4vA96ooZPv0tYqPxXAK+Jy5zw1aJZei79rl6mcTfD4mnvSor+ToB/onIdZ+L7TSdYbqS0kHkgc+9zPR6m8eExdaiT/wCrTuv4kbZ6MfScj0nxBqY3GOd9esPIOVHuAmmXls2YHifT/mDi8xa3e8AP1mS8Kdt5i1pFm3cZBgYGQzH7VgN+3wm7orR1fF1BSoU2d8r6o7qj7ztsVeZne6V6KYTRujW7ZQ+JqEBag1rLUvcInBQAb/eseQGblIsxtcEigSLyRY7hINNMsDCd91RYHXxVWvuo09UZfbqHL3I/rODbbLY6oKdsLiWt7VYC/HVRDb+r3yCwYrwihDihCQF4QhKJQkYQJtFeJjnFeFBMRMCZEmAma2Z85z2MwuA0k6Oz9sKWsFWnU+r7xFywQ3z1RtO6bPSjTAweFqV+6WXVCK2x3JHd9NbyBnA1utdiv/SnW3gVQVHnb9JnLfpvDx/ZaWHphAqKgVUAC21bADICZtUHcJ4vRfFYmtSFXE01p9oFammuWcIRtfIapOWWdt+eQ9s1AJx072/TX0h2SU3esVCIpNQv7IXnx4W33lJ6fr4Kq5GFwiUlBNmu4qNz1A2oo5WPiJ2fWvpNhTw+HUkCozvUtv1NUKDyu5PkJWfaTrhjO3LO3pu6Oxb4WolWg2o6X1GCqSLgg5EEHInbNLEo1R3qFu9UZnfLazEsSLbMyY0JMlr3ynRzee1FlJJF/CO83dWM077YRoE5zo+h3RmppKrYXSlTI7d+G/US+1z7gbncD4r4dOflOi0X0qxeFSnToPTSnTz1BSQqx2kuxGsSTtN5Lv0uOt8rjwGj8LgKJSlTSkgzdr95iB7TMc2NhtMp7pn0gfSFfWViKNO60F4je55t7gBznqaV6yKtanUo9giGquoXDayqhyZdVhtIO2+7ZOMZwJjHGzmt5ZTWoV9xmNzMhsd4mGtlvnRzYWO08JfvQzRZwmBw9JvbK69T8b94jyuF/LKc6HaJOMxtGkRdAdet/lIQWB8TZfzS/wAmRDvC8UIBCKEBwiheBKEISAY5mImDGRvKoJkCYEyBMo4HrcwzvhqFRSdWnUZag3Xde63lqkfnlZ6MdaFWnUamrimysUb2Wsb2MvbpFo76XhK1DLWdb07/AOIpDJ/UBKHqnUJDAgi4IIsQRkQRxhY97SHTzSD1NdHSmu5AocW5kj4Wkl6ydIAWYUm5hWB+JnLEFjJ9naZ8Yvlft6mkdPV8cQ9fV7msqBb2ANifgPSagmtTfVmY1BLJpLd9sjNugrTEHvJNslGwGkHcnITEjx3hGVRaS1phFTKIvYX8IU0s2vfex90iG2qdo96yWHW1/EwqpsYbR8N8IiUEwEZzIz2ymXRuCfE1qdCn7VV1RTwvta3AC58pBafVRons8PUxTDvYg6qX/wAJCRfzbW/lWd9ea+DwqUadOlTFkpoqIOCqLD4TLCJEyMIQHeF4oQCEUIE7wkYQG20yJhCVUWmOEIClE9M/+vxf+bU+MIQPGp7ZlqbIQhWqZB/a9IQijYWZ4QgYU2mZTshCERSFTYYQhWWnsk4QhGm+/wA503Vv/wC6Ybwrf/U8cJBeJihCVBCEJAQhCAoQhAcIQgf/2Q==",
  },
];

async function submitPreferences() {
  //give me outdoor activities that can done in a group of 3. location and price within 20-30 in singapore and description
  //get from ai
  loading.value = true;
  submitted.value = true;
  displayUsers.value = users.slice(0, numPeople.value);
  const prompt =
    "Provide me a list of " +
    placeType.value +
    " activities that can be done in Singapore in a group of " +
    numPeople.value +
    1 +
    " and is within the budget of " +
    minimum.value +
    " and " +
    maximum.value +
    ". Provide the name, location, price, description. Provide data in an array of json format with name, location, price, description as keys. follow the format { name: 'Indoor Skydiving',location: 'iFly Singapore, Sentosa',price: '40 - 50 SGD per person', description:'Experience the thrill of skydiving in a vertical wind tunnel, perfect for adventure seekers.'}";

  try {
    const response = await axios.post("http://localhost:8080/api/safe", {
      content: prompt,
    });
    groupActivities.value = JSON.parse(response.data);
    loading.value = false;
  } catch (error) {
    groupActivities.value = [
      {
        name: "Indoor Skydiving",
        location: "iFly Singapore, Sentosa",
        priceRange: "40 - 50 SGD per person",
        description:
          "Experience the thrill of skydiving in a vertical wind tunnel, perfect for adventure seekers.",
      },
      {
        name: "Escape Room Challenge",
        location: "Various locations in Singapore",
        price: "40 - 50 SGD per person",
        description:
          "Solve puzzles, find clues, and escape from themed rooms within a time limit. Great for testing your teamwork and problem-solving skills.",
      },
      {
        name: "Virtual Reality Gaming",
        location: "Various VR arcades in Singapore",
        price: "40 - 50 SGD per person",
        description:
          "Immerse yourself in exciting virtual worlds and play multiplayer games with your friend in VR.",
      },
      {
        name: "Cooking Class",
        location: "Various cooking schools in Singapore",
        price: "40 - 50 SGD per person",
        description:
          "Learn to prepare delicious dishes from expert chefs and enjoy a hands-on cooking experience.",
      },
      {
        name: "Indoor Trampoline Park",
        location: "Bounce Singapore, Cineleisure Orchard",
        price: "40 - 50 SGD per person",
        description:
          "Jump and flip to your heart's content on interconnected trampolines in a fun and energetic environment.",
      },
    ];
  }
}
</script>
